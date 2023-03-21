# -*- coding: cp1251 -*-

# First Bot

import random
import telebot
import json
from pars_horoscope import zodiak

token = '6063376644:AAG_y0YYtQ1vW0yjt72QFFBucH5GGhFNOAQ'

bot = telebot.TeleBot(token)

with open('horoscope.json', 'r', encoding = 'utf-8') as horo:
	horoscope_dict = json.load(horo)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Добро пожаловать!')
	welcome(message)

@bot.message_handler(content_types=['text'])
def welcome(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = telebot.types.KeyboardButton('Рандомное число')
	item2 = telebot.types.KeyboardButton('Кинуть кость')
	item3 = telebot.types.KeyboardButton('Как дела?')
	item4 = telebot.types.KeyboardButton('Сжать')
	item5 = telebot.types.KeyboardButton('Загадай число')
	item6 = telebot.types.KeyboardButton('Гороскоп')
	item7 = telebot.types.KeyboardButton('Покажи id стикера')

	markup.add(item1, item2, item3, item4, item5, item6, item7)

	bot.send_message(message.chat.id, 'Чем зймемся?', reply_markup=markup)

	bot.register_next_step_handler(message, answer)


@bot.message_handler(content_types=['text'])
def answer(message):
	if message.text.lower() == 'рандомное число':
		bot.send_message(message.chat.id, str(random.randint(1, 10)))

	elif message.text.lower() == 'кинуть кость':
		bot.send_message(message.chat.id, f'Ваше число: {str(random.randint(1, 7))}')

	elif message.text.lower() == 'как дела?':
		bot.send_message(message.chat.id, 'Довольно неплохо')

	elif message.text.lower() == 'гороскоп':

		markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

		item1 = telebot.types.KeyboardButton('Овен')
		item2 = telebot.types.KeyboardButton('Телец')
		item3 = telebot.types.KeyboardButton('Близнецы')
		item4 = telebot.types.KeyboardButton('Рак')
		item5 = telebot.types.KeyboardButton('Лев')
		item6 = telebot.types.KeyboardButton('Козерог')
		item7 = telebot.types.KeyboardButton('Весы')
		item8 = telebot.types.KeyboardButton('Скорпион')
		item9 = telebot.types.KeyboardButton('Водолей')
		item10 = telebot.types.KeyboardButton('Стрелец')
		item11 = telebot.types.KeyboardButton('Дева')
		item12 = telebot.types.KeyboardButton('Рыбы')
		item13 = telebot.types.KeyboardButton('Выйти')

		markup2.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

		bot.send_message(message.chat.id, 'Выберите знак зодиака', reply_markup=markup2)

		bot.register_next_step_handler(message, horoscope)

	elif message.text.lower() == 'загадай число':
		global number
		number = random.randint(1, 11)
		bot.send_message(message.chat.id, 'Загадал')
		bot.register_next_step_handler(message, guess_the_number)

	else:
		bot.send_message(message.chat.id, 'Я пока не умею отвечать на такие сообщения')

@bot.message_handler(content_types=['text'])
def guess_the_number(message):
	if message.text.lower() == f'{number}':
		bot.send_message(message.chat.id, 'Угадали!')
		welcome(message)

	elif message.text.lower() > f'{number}':
		bot.send_message(message.chat.id, 'Меньше!')
		bot.register_next_step_handler(message, guess_the_number)

	elif message.text.lower() < f'{number}':
		bot.send_message(message.chat.id, 'Больше!')
		bot.register_next_step_handler(message, guess_the_number)

@bot.message_handler(content_types=['text'])
def horoscope(message):
	if message.text != 'Выйти':
		bot.send_message(message.chat.id, zodiak(horoscope_dict[message.text]))
		bot.register_next_step_handler(message, horoscope)
	else:
		welcome(message)


bot.polling(none_stop = True)