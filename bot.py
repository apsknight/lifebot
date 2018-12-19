#!/usr/bin/env python

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging
from symptoms import HealthCare
from translate import translate_from_english, translate_to_english

client = HealthCare()
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LANGUAGE, GENDER, AGE, LOCATION, BIO = range(5)

lang_map = {
    "English" : "en",
    "हिंदी" : "hi",
    "मराठी" :  "mr",
    "বাংলা" : "bn"
}

def start(bot, update):
    reply_keyboard = [["English", "हिंदी"], ["मराठी", "বাংলা"]]
    lang_pick = "Please select your language.\nअपना भाषा चुनें।\nकृपया तुमची भाषा निवडा\nআপনার ভাষা নির্বাচন করুন"
    update.message.reply_text(lang_pick,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return LANGUAGE

def language(bot, update, user_data):
    reply_keyboard = [['Male', 'Female'], ['Other']]
    user = update.message.from_user
    text = update.message.text
    user_data["lang"] = lang_map[text]
    welcome_text = "Hi {}! I will help you with your medical conditions.\nSend /cancel to stop talking to me.\n\nPlease select your Gender.".format(user.first_name)
    update.message.reply_text(translate_from_english(welcome_text, user_data["lang"]),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER

def gender(bot, update, user_data):
    user = update.message.from_user
    text = update.message.text
    user_data["gender"] = text
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    reply = 'I see! Please tell me about your Age, so I can detect disease easily.'
    update.message.reply_text(translate_from_english(reply, user_data["lang"]), reply_markup=ReplyKeyboardRemove())

    return AGE


def age(bot, update, user_data):
    user = update.message.from_user
    text = update.message.text
    user_data["age"] = text
    logger.info("Age of %s: %s", user.first_name, update.message.text)
    reply = 'Thank You! Now, send me your location please. I\'ll search nearby doctors from your location.'
    update.message.reply_text(translate_from_english(reply, user_data["lang"]))

    return LOCATION


def skip_age(bot, update, user_data):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)

    reply = 'You do not want to tell you age, That\'s Okay. Please share your location, so that I can look for doctors nearby.'
    update.message.reply_text(translate_from_english(reply, user_data["lang"]))

    return LOCATION


def location(bot, update, user_data):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    user_data["location"] = str(user_location.latitude) + '/' + str(user_location.longitude)

    reply = 'Thank You for telling your location. At last, tell me about your problems.'
    update.message.reply_text(translate_from_english(reply, user_data['lang']))

    return BIO


def skip_location(bot, update, user_data):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    reply = 'You seem a bit paranoid! At last, tell me what are you suffering from?'
    update.message.reply_text(translate_from_english(reply, user_data['lang']))
    return BIO


def bio(bot, update, user_data):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    reply1 = 'Thank you! I\'ll reply about your problems soon.'
    update.message.reply_text(translate_from_english(reply1, user_data['lang']))
    query = translate_to_english(update.message.text)
    result = client.getConditionfromText(query)

    if result['status'] != 'ok':
        sorryMsg = 'Sorry, I was unable to find details for these symptoms.'
        update.message.reply_text(translate_from_english(sorryMsg, user_data['lang']))
    for k, v in result.items():
        if k != 'status':
            category = translate_from_english(k, user_data['lang'])
            msg = translate_from_english(v, user_data['lang'])
            update.message.reply_text(category + ': ' + msg)

    doctors = client.getNearestDoctor()
    result = 'Nearest Doctors: \n'
    for doctor in doctors:
        result = result + doctor + ',\n\n'

    update.message.reply_text(translate_from_english(result, user_data['lang']))

    return BIO


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! Stay Healthy :).',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    print('Starting..!')
    logger.info("Waking Up Bot.")
    updater = Updater("Token")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LANGUAGE: [RegexHandler('^(English|हिंदी|मराठी|বাংলা)$', language, pass_user_data=True)],

            GENDER: [RegexHandler('^(Male|Female|Other)$', gender, pass_user_data=True)],

            AGE: [RegexHandler('^[1-9][0-9]{0,1}$', age, pass_user_data=True),
                    CommandHandler('skip', skip_age, pass_user_data=True)],

            LOCATION: [MessageHandler(Filters.location, location, pass_user_data=True),
                       CommandHandler('skip', skip_location, pass_user_data=True)],

            BIO: [MessageHandler(Filters.text, bio, pass_user_data=True)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    logger.info("Bot is polling for sessions.")
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()