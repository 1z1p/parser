import requests
from bs4 import BeautifulSoup as BS 
import csv
from time import sleep

x = int(input("Введите сколько страниц с парсить: "))
for i in range(1,x):
	url = f'https://howdyho.net/top-100/page/{str(i)}'
	HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 YaBrowser/21.2.3.100 Yowser/2.5 Safari/537.36','accept':'*/*'}
	HOST = 'https://howdyho.net'
	FILE = 'prog.csv'
	
	
	def get_html(url, params = None):
		re = requests.get(url, headers = HEADERS, params = params)
		return re
	
	def get_content(html):
		
		soup = BS(html, 'html.parser')
		items = soup.find_all('article', class_='over100k')
		items_2 = soup.find_all('article', class_='over10k')
		items_3 = soup.find_all('article', class_='over5k')
		ca = []
		for item in items:
			ca.append({
				'title': item.find('a').get_text(strip = True),
				'download_t': item.find('span', class_='status').get_text(strip = True),
				'datetime': item.find('span', class_='pubdate').get_text(strip = True),
				'download_d': HOST + item.find('img').get('src'),
				'download': HOST + item.find('a', class_='btn-green').get('href')
			})
		for item in items_2:
			ca.append({
				'title': item.find('a').get_text(strip = True),
				'download_t': item.find('span', class_='status').get_text(strip = True),
				'datetime': item.find('span', class_='pubdate').get_text(strip = True),
				'download_d': HOST + item.find('img').get('src'),
				'download': HOST + item.find('a', class_='btn-green').get('href')
			})
		for item in items_3:
			ca.append({
				'title': item.find('a').get_text(strip = True),
				'download_t': item.find('span', class_='status').get_text(strip = True),
				'datetime': item.find('span', class_='pubdate').get_text(strip = True),
				'download_d': HOST + item.find('img').get('src'),
				'download': HOST + item.find('a', class_='btn-green').get('href')
			})
		return ca
	def save_xls(items, path):
		with open(path, 'a', newline = '') as file:
			writer = csv.writer(file, delimiter = ';')
			for item in items:
				writer.writerow([item['title'],item['download_t'],item['datetime'],item['download_d'],item['download']])
	
	def parse():
		html = get_html(url)
		if html.status_code == 200:
			
			cars = get_content(html.text)
			print(f'{len(cars)} программ добавлены в файл.')
			save_xls(cars, FILE)
			sleep(20)
		else:
			print('Error')
	parse()
input()