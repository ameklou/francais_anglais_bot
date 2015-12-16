#coding: utf-8

from telegram import Updater
from yandex_translate import YandexTranslate

updater = Updater(token='112262702:AAHLgpm06rXHWtPYFJ_RwLPbw3M_RFwexcA')
dispatcher = updater.dispatcher
translate = YandexTranslate('trnsl.1.1.20151214T002932Z.b551b8b2ddb7845d.b1190d5048ddedd9ce60023e4a580d62dfa03704')


def reformatter_la_traduction(original):
	la_traduction_formater = original.replace(u'@Francais_Anglais_bot','')
	la_traduction_formater = original.replace(u'/tofrench','')
	la_traduction_formater = original.replace(u'/enchinois','')
	la_traduction_formater = original.replace(u'/enhebreux','')
	la_traduction_formater = original.replace(u'/enallemand','')
	
	if la_traduction_formater.replace(' ','') == '':
		la_traduction_formater = u'Ajoutez moi du texte à traduire.'
	
	la_traduction_formater = u'Traduction: '+la_traduction_formater 
	return la_traduction_formater

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Salut ! Je suis un traducteur, je peux vous donner la traduction anglaise d'un mot français ou d'une phrase.")

def traduire(bot, update):
	global translate
	message_toen = update.message.text
	bot_traducteur = (translate.translate(message_toen, 'en'))
	traduction_original = bot_traducteur[u'text'][0]
	la_traduction = reformatter_la_traduction(traduction_original)
	bot.sendMessage(chat_id=update.message.chat_id, text = la_traduction)

def tofrench(bot, update, args):
	global translate
	message_tofr = ' '.join(args)
	bot_traducteur = (translate.translate(message_tofr, 'fr'))
	traduction_original = bot_traducteur[u'text'][0]
	la_traduction = reformatter_la_traduction(traduction_original)
	bot.sendMessage(chat_id=update.message.chat_id, text = la_traduction)


def enchinois(bot, update, args):
	global translate
	message_toch = ' '.join(args)
	bot_traducteur = (translate.translate(message_toch, 'zh'))
	traduction_original = bot_traducteur[u'text'][0]
	la_traduction = reformatter_la_traduction(traduction_original)
	bot.sendMessage(chat_id=update.message.chat_id, text = la_traduction)


def enhebreux(bot, update, args):
	global translate
	message_tohe = ' '.join(args)
	bot_traducteur = (translate.translate(message_tohe, 'he'))
	traduction_original = bot_traducteur[u'text'][0]
	la_traduction = reformatter_la_traduction(traduction_original)
	bot.sendMessage(chat_id=update.message.chat_id, text = la_traduction)

def enallemand(bot, update, args):
	global translate
	message_tohe = ' '.join(args)
	bot_traducteur = (translate.translate(message_tohe, 'nl'))
	traduction_original = bot_traducteur[u'text'][0]
	la_traduction = reformatter_la_traduction(traduction_original)
	bot.sendMessage(chat_id=update.message.chat_id, text = la_traduction)

def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text= u"Désolé je ne comprends pas cette commande.")


dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('tofrench', tofrench)
dispatcher.addTelegramCommandHandler('enchinois', enchinois)
dispatcher.addTelegramCommandHandler('enhebreux', enhebreux)
dispatcher.addTelegramCommandHandler('enallemand', enallemand)

dispatcher.addUnknownTelegramCommandHandler(unknown)
dispatcher.addTelegramMessageHandler(traduire)
updater.start_polling()