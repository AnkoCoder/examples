# an example of easy Telegram bot with buttons

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='Your token should be here', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    button_list = [
        [
            InlineKeyboardButton("Cake?", callback_data='cake'), 
            InlineKeyboardButton("Pie?", callback_data='pie')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(button_list)
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='Hey! Do you like cakes or pies better?', 
        reply_markup=reply_markup
    )

def cake(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='I like cakes too!'
    )

def pie(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='I like pies too!'
    )


start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(CallbackQueryHandler(cake, pattern='cake'))
dispatcher.add_handler(CallbackQueryHandler(pie, pattern='pie'))

updater.start_polling()