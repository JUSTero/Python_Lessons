# -*- coding: cp1251 -*-

from bs4 import BeautifulSoup
import requests

def zodiak(sign):
	url = f'https://horo.mail.ru/prediction/{sign}/today/'
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')
	prediction = soup.find(class_= "article__item article__item_alignment_left article__item_html")
	return prediction.text