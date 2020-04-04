import requests

#import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
token = '1107891137:AAE0111kLRMx5XDUWmrjCcoloov0jZgjVLI'





def start(update, context):
    update.message.reply_text(
        'Test'
    )
 #   return 'Initial'

def cancel(update, context):
    user = update.message.from_user
    print('Error Cancel')
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def echo(update, context):
    """Echo the user message."""
    print(update.message.text)
    update.message.reply_text(update.message.text)

def get_data():
    print('Message was sent to bot')

def covid_updates():
    print('Covid update engaged')
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
#    conv_handler = ConversationHandler(
#        entry_points=[CommandHandler('start', start)],
#        states = {
#            'Initial': [MessageHandler(Filters.text, get_data)]
#        },
#        fallbacks=[CommandHandler('cancel', cancel)]
#    )
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    covid_updates()
