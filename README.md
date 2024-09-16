
**Telegram Bot in Python**
This repository contains a simple Telegram bot built using Python. The bot is designed to interact with users in both private chats and groups, offering basic commands and responses to text messages. It's a great starting point for anyone looking to create their own bot and learn more about Python and the Telegram API.

Features
**Responds to commands such as /start, /help, and /custom.**
Custom responses to user messages based on keywords like "hello" and "how are you?"
Works in private chats and group chats, detecting when it's mentioned in a group.
Setup and Installation
To get started with this bot, follow these steps:

**Prerequisites**

Python 3.7+ should be installed on your machine. You can download it from the official Python website.
Install VS Code (recommended) and the Python extension for development.

Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/your-username/telegram-bot.git
cd telegram-bot
Step 2: Install the Required Libraries
You'll need to install a few Python libraries to interact with the Telegram API and work with databases:

bash
Copy code
pip install python-telegram-bot==20.3
pip install sqlalchemy
Step 3: Create a Telegram Bot Account
Open Telegram and search for BotFather.
Start a chat with BotFather and use the command /newbot.
Follow the instructions to create your bot and get an API token.
Replace the API_KEY and BOT_USERNAME placeholders in your code with your bot's token and username.
Step 4: Run the Bot
After setting up your token and username, you can run the bot:

bash
Copy code
python bot.py
The bot will start polling and waiting for messages.

How It Works
The bot defines a few key commands: /start, /help, and /custom. These commands trigger specific responses when typed in a chat with the bot.
It also listens for text messages, and based on certain keywords, it replies with custom responses. For example:
If the message contains "hello," it replies with "Whof Whof Hi."
If the message asks "how are you?" the bot responds with "awww good, thanks for asking."
It can also detect when it's mentioned in group chats, replying accordingly.
Example Commands
/start - Sends a greeting message.
/help - Offers assistance.
/custom - Sends a custom response.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
