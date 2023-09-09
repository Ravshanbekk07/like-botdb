from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from .db import DB


db = DB("db.json")


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    db.add(user.id, user.first_name)
    update.message.reply_text(
        text=f"Hi {user.first_name}!",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton("👍"), KeyboardButton("👎")]],
            resize_keyboard=True,
        )
    )


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="press one of the buttons below"
    )


def like(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    db.inc_like(user.id)
    update.message.reply_text(
        text=f"you have {db.data[str(user.id)]['likes']} likes and {db.data[str(user.id)]['dislikes']} dislikes."
    )


def dislike(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    db.inc_dislike(user.id)
    update.message.reply_text(
        text=f"you have {db.data[str(user.id)]['likes']} likes and {db.data[str(user.id)]['dislikes']} dislikes."
    )

