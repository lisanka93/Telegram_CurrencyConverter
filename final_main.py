import telebot
from config import *
from utils import *



bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["start"])
def greet(message):
    bot.send_message(message.chat.id, f"Hey {message.chat.username}!\nI am a currency converter bot. I support over 150 physical currencies and over 550 digital currencies. For a list of popular physical currencies type /pcurrencies and for a list of populat digital currencies type /dcurrencies. To convert a currency please write it in the following format: <from_currency code> <to_currency code> <money-value>. For example: USD RUB 100")

@bot.message_handler(commands=["pcurrencies"])
def currencies(message):
    bot.reply_to(message, fmtpairs(PCURRENCIES))

@bot.message_handler(commands=["dcurrencies"])
def currencies(message):
    bot.reply_to(message, fmtpairs(DCURRENCIES))

@bot.message_handler(content_types = CONTENT_TYPES)
def repeat(message):
    bot.send_message(message.chat.id, "Sorry I do not handle this type of input.")

@bot.message_handler(content_types =["text"])
def convert_currency(message):
    try:
        converted = CurrencyConverter.convert(message.text)
        bot.send_message(message.chat.id, converted)
    except CurrencyException as e:
        bot.send_message(message.chat.id, e)
    except Exception as e:
        message = "I am sorry but it seems like the server is down 🥺"
        bot.send_message(message.chat.id, message)



print("bot is working...")
bot.polling() #checking for new incoming messages
