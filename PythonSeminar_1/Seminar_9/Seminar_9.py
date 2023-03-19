# -*- coding: cp1251 -*-

# First Bot

import random
import telebot
import json

token = '6063376644:AAG_y0YYtQ1vW0yjt72QFFBucH5GGhFNOAQ'

bot = telebot.TeleBot(token)

with open('horoscope.json', 'r') as horo:
	horoscope_dict = json.load(horo)

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = telebot.types.KeyboardButton('��������� �����')
	item2 = telebot.types.KeyboardButton('������ �����')
	item3 = telebot.types.KeyboardButton('��� ����?')
	item4 = telebot.types.KeyboardButton('�����')
	item5 = telebot.types.KeyboardButton('������� �����')
	item6 = telebot.types.KeyboardButton('��������')
	item7 = telebot.types.KeyboardButton('������ id �������')

	markup.add(item1, item2, item3, item4, item5, item6, item7)

	bot.send_message(message.chat.id, '����� ����������! �������� ������ ��� ����� ����: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
	if message.text.lower() == '��������� �����':
		bot.send_message(message.chat.id, str(random.randint(1, 10)))

	elif message.text.lower() == '������ �����':
		bot.send_message(message.chat.id, f'���� �����: {str(random.randint(1, 7))}')

	elif message.text.lower() == '��� ����?':
		bot.send_message(message.chat.id, '�������� �������')

	elif message.text.lower() == '��������':

		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

		item1 = telebot.types.KeyboardButton('����')
		item2 = telebot.types.KeyboardButton('�����')
		item3 = telebot.types.KeyboardButton('��������')
		item4 = telebot.types.KeyboardButton('���')
		item5 = telebot.types.KeyboardButton('���')
		item6 = telebot.types.KeyboardButton('�������')
		item7 = telebot.types.KeyboardButton('����')
		item8 = telebot.types.KeyboardButton('��������')
		item9 = telebot.types.KeyboardButton('�������')
		item10 = telebot.types.KeyboardButton('�������')
		item11 = telebot.types.KeyboardButton('����')
		item12 = telebot.types.KeyboardButton('����')

		markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

		bot.send_message(message.chat.id, '�������� ���� �������', reply_markup=markup)

		bot.register_next_step_handler(message, horoscope)

	elif message.text.lower() == '������� �����':
		global number
		number = random.randint(1, 11)
		bot.send_message(message.chat.id, '�������')
		bot.register_next_step_handler(message, guess_the_number)

	else:
		bot.send_message(message.chat.id, '� ���� �� ���� �������� �� ����� ���������')

@bot.message_handler(content_types=['text'])
def guess_the_number(message):
	if message.text.lower() == f'{number}':
		bot.send_message(message.chat.id, '�������!')

	elif message.text.lower() > f'{number}':
		bot.send_message(message.chat.id, '������!')
		bot.register_next_step_handler(message, guess_the_number)

	elif message.text.lower() < f'{number}':
		bot.send_message(message.chat.id, '������!')
		bot.register_next_step_handler(message, guess_the_number)

@bot.message_handler(content_types=['text'])
def horoscope(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

	item13 = telebot.types.KeyboardButton('�����')

	markup.add(item13)

	if message.text != '�����':
		bot.send_message(message.chat.id, horoscope_dict[message.text], reply_markup = markup)
		bot.register_next_step_handler(message, horoscope)
	else:
		bot.register_next_step_handler(message, welcome)


bot.polling(none_stop = True)

