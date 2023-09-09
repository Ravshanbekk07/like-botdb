from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import os
from dotenv import load_dotenv
from .handlers import start, help, like, dislike, inline, like_query, dislike_query


load_dotenv()

token = os.getenv("TOKEN")

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("inline", inline))
    dispatcher.add_handler(MessageHandler(Filters.text("👍"), like))
    dispatcher.add_handler(MessageHandler(Filters.text("👎"), dislike))
    dispatcher.add_handler(CallbackQueryHandler(pattern="dislike", callback=dislike_query))
    dispatcher.add_handler(CallbackQueryHandler(pattern="like", callback=like_query))

    updater.start_polling()
    updater.idle()