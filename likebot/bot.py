from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv
from .handlers import start, help, like, dislike


load_dotenv()

token = os.getenv("TOKEN")

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text("👍"), like))
    dispatcher.add_handler(MessageHandler(Filters.text("👎"), dislike))

    updater.start_polling()
    updater.idle()