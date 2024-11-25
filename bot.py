from openai import AzureOpenAI
import os
import json
import requests

client = AzureOpenAI(
	api_key = os.getenv("AZURE_KEY"),
	api_version = "2023-10-01-preview",
	azure_endpoint = os.getenv("AZURE_ENDPOINT")
)

with open('ticketmaster_key.txt','r') as key_file:
    ticketmaster_key = key_file.read()

messages = [
	{"role": "system", "content":"Say everything funny and from an artist perspective recommendation"},
	{"role":"user", "content":"Find concerts in London in year 2025 by adding the dates and venue"}

]

def concerts(start_date,end_date):   
	dma_id = 601
	url = (f"https://app.ticketmaster.com/discovery/v2/events.json?"
       f"classificationName=music&countryCode=GB&"
       f"startDateTime={start_date}&endDateTime={end_date}&"
       f"dmaId={dma_id}&size=200&apikey={ticketmaster_key}")
	
	response = requests.get(url)
	data = response.json()
	return f"Concerts in London from{start_date} to {end_date}"

functions = [
	{
		"type": "function",
		"function": {
			"name": "Find_concerts",
			"description": "Find the concerts in London in year 2025",
			"parameters": {
				"type": "object",
				"properties": {
					"start_date": {
						"type": "string",
						"description": "The start_date that I want to look up"
					},
					"end_date":{
						"type":"string",
						"description": "The end_date that I want to look up."
					},
				},
				"required": ["start_date","end_date"]
			}
		}
	}
]

response = client.chat.completions.create(
	model = "GPT-4",
	messages=messages,
	tools=functions,
	tool_choice="auto"
	
)

response_message= response.choices[0].message
gpt_tools = response.choices[0].message.tool_calls

if gpt_tools:
	available_functions ={
		"Find_concerts": concerts
	}

	messages.append(response_message)
	for gpt_tool in gpt_tools:
		function_name = gpt_tool.function.name
		function_to_call = available_functions[function_name]

		function_parameters = json.loads(gpt_tool.function.arguments)
		function_response =function_to_call(function_parameters.get('start_date'),function_parameters.get('end_date'))
		
		messages.append(
			{
				"tool_call_id": gpt_tool.id,
				"role": "tool",
				"name": function_name,
				"content": function_response
			}
		)
		second_response = client.chat.completions.create(
			model = "GPT-4",
			messages=messages
		)
		print(second_response.choices[0].message.content)


else:
	print(response.choices[0].message.content)