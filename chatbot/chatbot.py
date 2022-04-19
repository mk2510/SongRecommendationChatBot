from telegram.ext import Updater
import os
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

TOKEN = '5395404180:AAFLELsZHTR4c1zZkO_we7_lMcQtfAui8yU'
updater = Updater(token=TOKEN, use_context=True)

PORT = int(os.environ.get('PORT', 5000))

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update: Update, context: CallbackContext):
    t = ("Hello %s, this is SongRecommenderBot. What kind of Taylor's song would you like to listen?" + "\n" + "Type /song followed by a list of key-words. If you struggle, type /help.") % update.message.chat.first_name
    context.bot.send_message(chat_id=update.effective_chat.id, text=t)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://localhost/' + TOKEN)


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Infered Message')
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)