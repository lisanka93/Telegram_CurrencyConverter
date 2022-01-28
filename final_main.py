import telebot
from telebot import types
from config import *
from utils import *
from keys import *


bot = telebot.TeleBot(API_KEY)

user_dict = {}   #needs to be replaced with redis database!


@bot.message_handler(commands=["start"])
def language(message):
    cid = message.chat.id

    if cid not in user_dict:
        user_dict[cid] = ""

    markup = types.InlineKeyboardMarkup()
    b = types.InlineKeyboardButton("English",callback_data='eng')
    c = types.InlineKeyboardButton("Русский",callback_data='rus')
    markup.add(b,c)
    bot.send_message(message.chat.id, "Select language / Выберите язык", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    if call.message:
        if call.data == "eng":
            cid = call.message.chat.id
            user_dict[cid] = "eng"
            bot.answer_callback_query(callback_query_id=call.id)
            bot.send_message(call.message.chat.id, f"Hey {call.message.chat.username}!\nI am a currency converter bot. I support over 150 physical currencies and over 550 digital currencies. For a list of popular physical currencies type /pcurrencies and for a list of popular digital currencies type /dcurrencies. To convert a currency please write it in the following format: <from_currency code> <to_currency code> <money-value>. For example: USD RUB 100")

    if call.message:
        if call.data == "rus":
            cid = call.message.chat.id
            user_dict[cid] = "rus"
            bot.answer_callback_query(callback_query_id=call.id)
            bot.send_message(call.message.chat.id, text=f"Привет {call.message.chat.username}!\nЯ бот-конвертер валют. Я поддерживаю более 150 физических валют и более 550 цифровых валют. Для списка популярных физических валют введите /pcurrencies, а для списка популярных цифровых валют введите /dcurrencies. Чтобы конвертировать валюту, напишите ее в следующем формате: <от_код_валюты> <на_код_валюты> <денежное значение>. Например: USD RUB 100.")


@bot.message_handler(commands=["help"])
def greet(message):
    cid = message.chat.id
    lang =user_dict[cid]
    if lang == "rus":
        bot.send_message(message.chat.id, text=f"Для списка популярных физических валют введите /pcurrencies, а для списка популярных цифровых валют введите /dcurrencies. Чтобы конвертировать валюту, напишите ее в следующем формате: <от_код_валюты> <на_код_валюты> <денежное значение>. Например: USD RUB 100")
    else:
        bot.send_message(message.chat.id, f"For a list of popular physical currencies type /pcurrencies and for a list of popular digital currencies type /dcurrencies. To convert a currency please write it in the following format: <from_currency code> <to_currency code> <money-value>. For example: USD RUB 100")


@bot.message_handler(commands=["pcurrencies"])
def currencies(message):
    bot.reply_to(message, fmtpairs(PCURRENCIES))

@bot.message_handler(commands=["dcurrencies"])
def currencies(message):
    bot.reply_to(message, fmtpairs(DCURRENCIES))

@bot.message_handler(content_types = CONTENT_TYPES)
def repeat(message):
    cid = message.chat.id
    lang =user_dict[cid]
    if lang == "rus":
        bot.send_message(message.chat.id, "Извините, я не обрабатываю этот тип ввода")
    else:
        bot.send_message(message.chat.id, "Sorry I do not handle this type of input")

@bot.message_handler(content_types =["text"])
def convert_currency(message):
    cid = message.chat.id
    lang =user_dict[cid]
    try:
        converted = CurrencyConverter.convert(message.text, lang)
        bot.send_message(message.chat.id, converted)
    except CurrencyException as e:
        bot.send_message(message.chat.id, e)
    except Exception as e:
        if lang == "rus":
            message = "Прошу прощения, но похоже сервер не работает 🥺"
            bot.send_message(message.chat.id, message)
        else:
            message = "I am sorry but it seems like the server is down 🥺"
            bot.send_message(message.chat.id, message)


print("bot is working...")
bot.polling() #checking for new incoming messages
