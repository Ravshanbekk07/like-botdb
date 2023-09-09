from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
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


def inline(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(
        text=f"you can press one of the buttons below",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("👍:0", callback_data="like:0"), InlineKeyboardButton("👎:0", callback_data="dislike:0")]],
        )
    )


def like_query(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer("you pressed like")

    likes = int(query.data.split(":")[1])
    likes += 1

    markup = update.callback_query.message

    markup.reply_markup.inline_keyboard

    query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"👍:{likes}", callback_data=f"like:{likes}"), markup.reply_markup.inline_keyboard[0][1]]],
        )
    )

def dislike_query(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer("you pressed dislike")

    dislikes = int(query.data.split(":")[1])
    dislikes += 1

    markup = update.callback_query.message

    markup.reply_markup.inline_keyboard

    query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(
            [[markup.reply_markup.inline_keyboard[0][0], InlineKeyboardButton(f"👎:{dislikes}", callback_data=f"dislike:{dislikes}")]],
        )
    )