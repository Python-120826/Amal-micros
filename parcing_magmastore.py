import requests
from bs4 import BeautifulSoup
url_of_magmastore = 'https://magmastore.uz/'
catalog = 'tekstil/'
major = url_of_magmastore+catalog
Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
html = requests.get(major, headers=Headers)


soup = BeautifulSoup(html.content, 'html.parser')
links = soup.find_all('a', href=True)

print (f'всего ссылок в этой категории :',len(links))
print(soup.get_text())
