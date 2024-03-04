from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('6903266291:AAGMF6MhUlWeMmsUGFGbRWYBQo0btfwA1E8')

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    full_name=message.from_user.full_name
    bot.send_message(chat_id,f"Assalomu alaykum {full_name}")


bot.polling()