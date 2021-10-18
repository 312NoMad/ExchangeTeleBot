import telebot
from telebot import types

from api import get_currency_list
from mytoken import Token

bot = telebot.TeleBot(Token)

# Home keyboard
keyboard = types.ReplyKeyboardMarkup()
key_list = types.KeyboardButton(text='Get currency list')
key_exchange = types.KeyboardButton(text='Exchange')
keyboard.row(key_list, key_exchange)

# Exchange keyboard
keyboard1 = types.ReplyKeyboardMarkup()
key_usd = types.KeyboardButton(text='USD')
key_eur = types.KeyboardButton(text='EUR')
keyboard1.row(key_usd, key_eur)

value = 0
currency1 = ''
currency2 = ''

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Can I help you?', reply_markup=keyboard)
        bot.register_next_step_handler(message, get_operation)
    else:
        bot.send_message(message.from_user.id, 'Click /start')


def get_operation(message):
    if message.text == 'Get currency list':
        bot.send_message(message.from_user.id, get_currency_list())
        bot.register_next_step_handler(message, get_operation)
    else:
        bot.send_message(message.from_user.id, 'What currency you want to convert', reply_markup=keyboard1)
        bot.register_next_step_handler(message, get_currency1)


def get_currency1(message):
    global currency1
    currency1 = message.text
    bot.send_message(message.from_user.id, 'What value you want to convert')
    bot.register_next_step_handler(message, get_exchange_value)


def get_exchange_value(message):
    global value
    value = int(message.text)
    bot.send_message(message.from_user.id, 'What currency you want to get')
    bot.register_next_step_handler(message, get_currency2)


def get_currency2(message):
    global currency2
    currency2 = message.text


bot.polling()
