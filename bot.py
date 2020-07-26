import telebot

import config
import services

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def repeat_all_messages(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda m: True)
@bot.message_handler(content_types=['text'])
def echo_all(message):
    date = message.text
    text = services.parse(date)
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling()
