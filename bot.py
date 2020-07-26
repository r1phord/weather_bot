import telebot

import config
import services

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, "Для получения прогноза погоды, введите дату. Пример ввода: 17 августа")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    date = message.text
    text = services.parse(date)
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling()
