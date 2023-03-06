import requests
from bs4 import BeautifulSoup as BS
from pprint import pp


URL = 'https://mashina.kg'
response = requests.get(URL)
# print(response.status_code)
# print(response)
# pp(response)
# pp(dir(response))
#
# print(response.text[:200])

soup = BS(response.text, "html.parser")
table = soup.find('div', class_="category-block-content")
cars = []
for obyava in table.findAll('a'):
    car = {}
    car['name'] = obyava.find('h2'.class_="name")
    car['price'] = obyava.find('div', class_="block price").find('strong')

    cars.append(car)
    pprint(cars)

    # print(obyava.text.strip().replace(' ',''))