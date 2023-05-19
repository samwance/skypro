import random
import requests
from basic_word import BasicWord


def load_random_word():
    """
    Загружает случайное слово
    """
    url = "https://www.jsonkeeper.com/b/5XYT"
    response = requests.get(url)
    data = response.json()
    random_word_data = random.choice(data)
    word = random_word_data["word"]
    subwords = random_word_data["subwords"]
    return BasicWord(word, subwords)
