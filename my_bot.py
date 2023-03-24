import telebot
from telebot import types

#taking control over the bot
bot = telebot.TeleBot("5989043694:AAE6u6rPQUr6Fd3Ve8Qv4aQ8xKBoy_FOJkA", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hi,<b>{message.from_user.first_name}</b>.\nThis is TESLA blog updated info.', parse_mode='html')
    
bot.polling(none_stop=True)