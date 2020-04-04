import requests
from call_covid_api import get_covid_data
from country_code_list import is_valid_country

#import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
token = '1107891137:AAE0111kLRMx5XDUWmrjCcoloov0jZgjVLI'





def start(update, context):
    update.message.reply_text(
        'Give me a country to look up for. It has to be ISO country code, like TH, CH, BR'
    )
 #   return 'Initial'

def cancel(update, context):
    user = update.message.from_user
    print('Error Cancel')
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

    
def echo(update, context):
    user_message = update.message.text
    if is_valid_country(user_message):
        display_data = get_covid_data(user_message)
        update.message.reply_text('Global Data:')
        update.message.reply_text('Confirmed Cases')
        update.message.reply_text(display_data['global_data']['global_confirmed'])
        update.message.reply_text('Deaths')
        update.message.reply_text(display_data['global_data']['global_deaths'])
        update.message.reply_text('Recovered')
        update.message.reply_text(display_data['global_data']['global_recovered'])
        update.message.reply_text('Fatality Rate')
        update.message.reply_text(display_data['global_data']['r_global_fatality_rate'])
        update.message.reply_text('Percentage of Global Popluation infected')
        update.message.reply_text(display_data['global_data']['r_global_p_of_pop_infected'])
    
    else:
        update.message.reply_text('Give me a country to look up for. Has to be ISO country code, like TH, CH, BR. Google it bro')
        

#def get_data():
#    print('Message was sent to bot')

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
