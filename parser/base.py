import requests
from bs4 import BeautifulSoup as BS
from db import get_cars
from pprint import pprint as pp

URL = "https://cars.kg/offers"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64;"
                         " x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
url = URL
response = requests.get(url, headers=headers)
print(response.status_code)


def remove_extra_spaces(text: str) -> str:
    """функция для обрезки лишних пробелов и переносов строки в тексте"""
    return ' '.join(text.replace('\n', '').split())


soup = BS(response.text, "html.parser")
table = soup.find('div', class_="catalog-list")
cars = []
for item in table.findAll('a', class_="catalog-list-item"):
    model = remove_extra_spaces(item.find(class_="catalog-item-params").text)
    price = remove_extra_spaces(item.find('span', class_="catalog-item-price").text)
    mileage = remove_extra_spaces(item.find('span', class_="catalog-item-mileage").text)
    info = remove_extra_spaces(item.find('span', class_="catalog-item-descr").text)
    cars.append((model, price, mileage, info))
get_cars(cars)
pp(cars)
