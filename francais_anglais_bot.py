#coding: utf-8

from telegram import Updater
import goslate

updater = Updater(token='112262702:AAHLgpm06rXHWtPYFJ_RwLPbw3M_RFwexcA')
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Salut ! Je suis un traducteur, je peux vous donner la traduction anglaise d'un mot français ou d'une phrase.")

def traduire(bot, update):
    message_fr = update.message.text
    bot_traducteur = goslate.Goslate()

    try:
    	message_en = bot_traducteur.translate(message_fr, 'en')
    except:
    	message_en = u"Désolé j'ai pas pu traduire cette phrase"

    bot.sendMessage(chat_id=update.message.chat_id, text = message_en)

def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text= u"Désolé je ne comprend pas les commandes.")

dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addUnknownTelegramCommandHandler(unknown)
dispatcher.addTelegramMessageHandler(traduire)
updater.start_polling()