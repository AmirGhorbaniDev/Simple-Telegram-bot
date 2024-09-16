
from typing import Final
# you can read more info regarding telegram library in offical docs https://github.com/python-telegram-bot/python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes
# you can ignore this part , you just need to add your Token in line 10 and your user name in line 12
from constants import API_KEY, BOT_USERNAME


## Call Final form typing module
TOKEN: Final = API_KEY
                # "Your API Key"
# Final will keep all Variant same , so it will not allow to change it
Bot_username : Final = BOT_USERNAME
                        # "Your Bot @Username"

# Commands

#async need to write before def to show that code reader show wait until recive answer 
async def start_command(update: Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ("Snif Sinf Hello")

async def help_command(update: Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ("Whof Whof how can i help you ?")

async def custom_command(update: Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ("What?")



# Response

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Whof Whof Hi"
    if "how are you ?" in processed:
        return "awww good , thanks for asking"
    if "how was your day?" in processed:
        return " fine !"
    
    return "whoooooof whoooof i dont understand"

async def handle_message(update : Update,context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == "group":
        if Bot_username in text:
            new_text: str = text.replace(Bot_username,"").strip()
            response: str = handle_response(text)

        else:
            return
    else:
        response : str = handle_response(text)

    print("bot:",response)
    await update.message.reply_text(response)

async def error(update : Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update{update}caused error {context.error}')

if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls
    print("Polling...")
    app.run_polling(poll_interval=3)