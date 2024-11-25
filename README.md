# Concert Finder Bot

This repository contains a Python-based bot that fetches concert information in London and provides entertaining responses, using OpenAI's GPT-4 model and the Ticketmaster API. The bot responds to concert-related queries with a fun and engaging tone, such as impersonating a singer.

------

## Features

- **OpenAI GPT-4 Integration**:
  - The bot uses OpenAI’s GPT-4 model to generate dynamic, conversational responses.
  - Customizable response style, with the ability to change the bot's persona (e.g., singer, comedian).
- **Concert Information**:
  - Retrieves concert details (such as event name, venue, and date) from the Ticketmaster API.
  - Allows users to specify the date range for concert queries.
- **Functionality**:
  - The bot can answer queries about concerts happening in a given date range.
  - Can integrate external API calls dynamically based on user input.

------

## Prerequisites

### Environment Variables

Before running the bot, make sure you set up the following environment variables:

1. **Azure OpenAI API**:
   - `AZURE_KEY`: Your Azure OpenAI API key.
   - `AZURE_ENDPOINT`: Your Azure OpenAI API endpoint.
2. **Ticketmaster API**:
   - Store your Ticketmaster API key in a file named `ticketmaster_key.txt` in the same directory as the script.

### Python Libraries

Ensure you have the following Python libraries installed:

```
pip install openai
pip install requests
```

------

## Setup and Usage

### 1. Set Up Your Environment

- Clone or copy the repository to your local machine.
- Create an environment file or set the required environment variables (`AZURE_KEY`, `AZURE_ENDPOINT`).
- Place your **Ticketmaster API key** in a file named `ticketmaster_key.txt`.

### 2. Run the Bot

You can run the bot by executing the Python script:

```
python bot.py
```

This will initiate the bot and start listening for concert queries.

### 3. Example Interaction

**User Input**:

```
Find concerts in London in 2025 by adding the dates and venue
```

**Bot Output** (with a singer persona):

```
🎶 "Hey, London! Here's what's coming your way in 2025:
- The Rolling Stones will be live at the O2 Arena on January 21st.
- Adele is making a triumphant return at the Royal Albert Hall on February 15th.
- And then we have Elton John lighting up the stage at the Wembley Stadium on March 3rd.
- Don't miss Rihanna at the SSE Arena on April 18th.
- Coldplay will be taking over the Twickenham Stadium on May 12th.

..." 🎤
```

The bot will retrieve concert details and respond in a fun, musical tone.