import telebot  # импортируем telebot
from secrets import secrets  # словарь с токеном из файла secrets.py
from telebot import types  # для определения типов
import random  # для выбора случайного комплимента
from compliments import compliments  # коллекция комплиментов
import os
import asyncio

# передаём значение переменной с кодом экземпляру бота
token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

# Хендлер для команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Инструкция к использованию")
    action_button = types.KeyboardButton("Комплимент")
    tetris_button = types.KeyboardButton("Тетрис")
    markup.add(start_button, action_button, tetris_button)

    bot.send_message(
        message.chat.id,
        text=f"Привет, {message.from_user.first_name} 👋\nСмелее, нажимай на кнопки",
        reply_markup=markup
    )

# Хендлер для обработки нажатий кнопок
@bot.message_handler(func=lambda message: message.text in ["Инструкция к использованию", "Комплимент", "Тетрис"])
def button_handler(message):
    if message.text == "Инструкция к использованию":
        bot.send_message(message.chat.id, "Нажми на кнопку Комплимент и подними себе настроение. Если стало скучно, то можешь поиграть в тетрис, нажав на соответствующую кнопку😊")
    elif message.text == "Комплимент":
        bot.send_message(message.chat.id, random.choice(compliments))
    elif message.text == "Тетрис":
        tetris_url = "https://tetris.com/play-tetris"
        markup = types.InlineKeyboardMarkup()
        tetris_button = types.InlineKeyboardButton("Играть!", url=tetris_url)
        markup.add(tetris_button)
        bot.send_message(message.chat.id, "Нажмите кнопку ниже, чтобы сыграть в Тетрис!", reply_markup=markup)

# Бесконечное выполнение кода
bot.polling(none_stop=True, interval=0)