import requests
from bs4 import BeautifulSoup

url = 'https://www.olx.uz/'
category = 'hobbi-otdyh-i-sport/antikvariat-kollektsii/'
major = url+category
html = requests.get(major)

soup = BeautifulSoup(html.content, 'html.parser')

print(html)

