import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.purina.ru/find-a-pet/articles/getting-a-cat/adoption/the-most-beautiful-cats'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    breeds = soup.find_all('h2')
    breed_list = [breed.get_text(strip=True) for breed in breeds]
    breed_list = breed_list[1:25]
else:
    print("Ошибка: не удалось получить страницу", response.status_code)

print("Давайте посмотрим какая кошечка подойдет Вам исходя из вашего знака зодиака.")
zodiac_sign = input("Введите свой знак зодиака: ").lower()
zodiac_letters = set(zodiac_sign)
matching_words = []
for word in breed_list:
    common_letters_count = len(zodiac_letters.intersection(set(word)))
    if common_letters_count >= 3:
        matching_words.append(word)


if matching_words:
    print("Вам с большой вероятностью подойдет порода:", random.choice(matching_words))
else:
    print("Вам лучше завести собачку...")