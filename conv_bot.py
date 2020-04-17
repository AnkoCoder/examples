# an easy Telegram bot with ConversationHandler

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='your token shoul be here', use_context=True)
dispatcher = updater.dispatcher

NAMES = 0
YEARS = 1
ANSWER = 2
TABLE = 3
AGAIN = 4

def hello(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='Hello! What is your name?'
    )
    return NAMES

def names(update, context):
    name = update.message.text
    context.user_data['name'] = name
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='How old are you, {}?'.format(name)
    )
    return YEARS


def years(update, context):
    years = update.message.text
    context.user_data['years'] = years
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='What do you like better: cakes or pies?'
    )
    return ANSWER


def answer(update, context):
    answer = update.message.text # update.message.text - the message which were given by user
    context.user_data['answer'] = answer # context.user_data is bot's dict where we can keep data for using it later in other funktions 
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='I like {} too! Isn\'t it cool?'.format(answer)
    )
    return TABLE

def table(update, context):
    name = context.user_data['name'] # getting info from context.user_data dict by using key's name 
    years = context.user_data['years']
    answer = context.user_data['answer']
    message = 'Your name is {} and you are {} years old, and also you like {} same as I do!'.format(name, years, answer)
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=message
    )
    return AGAIN

def again(update, context):
    if update.message.text == 'yes':
        return hello(update, context)
    else: 
        return context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text='Well....alright! Maybe next time!'
        )

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('hi', hello)],

    states={
        NAMES: [MessageHandler(Filters.text, names)],
        YEARS: [MessageHandler(Filters.text, years)],
        ANSWER: [MessageHandler(Filters.text, answer)],
        TABLE: [MessageHandler(Filters.text, table)], 
        AGAIN: [MessageHandler(Filters.text, again)]
    }, 

    fallbacks=[]
)

dispatcher.add_handler(conv_handler)


updater.start_polling()