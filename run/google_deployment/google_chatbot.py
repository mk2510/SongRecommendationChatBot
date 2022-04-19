import os
import http

from flask import Flask, request
from werkzeug.wrappers import Response

from telegram import Bot, Update
from telegram.ext import Dispatcher, Filters, MessageHandler, CallbackContext, CommandHandler

app = Flask(__name__)

TOKEN = '5395404180:AAFLELsZHTR4c1zZkO_we7_lMcQtfAui8yU'


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

bot = Bot(token=TOKEN)

def start(update: Update, context: CallbackContext):
    t = ("Hello %s, this is SongRecommenderBot. What kind of Taylor's song would you like to listen?" + "\n" + "Type /song followed by a list of key-words. If you struggle, type /help.") % update.message.chat.first_name
    context.bot.send_message(chat_id=update.effective_chat.id, text=t)

dispatcher = Dispatcher(bot=bot, update_queue=None)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

@app.post("/")
def index() -> Response:
    dispatcher.process_update(
        Update.de_json(request.get_json(force=True), bot))

    return "", http.HTTPStatus.NO_CONTENT