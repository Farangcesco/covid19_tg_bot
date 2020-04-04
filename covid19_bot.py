import requests
from call_covid_api import get_covid_data
from country_code_list import is_valid_country
from secret import token
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

def start(update, context):
    update.message.reply_text(
        'Give me a country to look up for. It has to be ISO country code, like TH, CH, BR'
    )

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
        
def covid_updates():
    print('Covid update engaged')
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    covid_updates()
