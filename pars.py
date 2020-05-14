from urllib.request import urlopen
from bs4 import BeautifulSoup

namepricedct = {}
for i in range(2000000000):
	
	htmlcode = urlopen('https://www.avito.ru/moskva/noutbuki').read().decode('utf-8')
	bscode = BeautifulSoup(htmlcode, features="html.parser")

	bsdiscrs = bscode.find_all('div', {'class': 'description item_table-description'})

	for bsdiscr in bsdiscrs:
		
		name = bsdiscr.find('a', {'class': 'snippet-link'}).get('title')
		namestart = name.find(' в Москве')
		name = name[:namestart:]
		
		price = str(bsdiscr.find('span', {'class': 'snippet-price'}))
		pricestart = price.find('\n')
		pricefinish = price.find('₽')
		price = price[pricestart + 1:pricefinish:]
		price = price.replace(' ', '')
		price = int(price)
		
		print(name, price)





