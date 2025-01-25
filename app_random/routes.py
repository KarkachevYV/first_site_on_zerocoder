from flask import Blueprint, render_template
import requests
from googletrans import Translator  # Убедитесь, что библиотека googletrans установлена

main = Blueprint('main', __name__)

API_KEY = 'YOUR_FAVQS_API_KEY'
BASE_URL = 'https://favqs.com/api/qotd'

@main.route('/')
def index():
    response = requests.get(BASE_URL, headers={"Authorization": f"Token token={API_KEY}"})
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data.get('quote', {}).get('body', 'No quote available')
        author = quote_data.get('quote', {}).get('author', 'Unknown')

        # Создание экземпляра Translator
        translator = Translator()

        # Перевод на русский
        quote = translator.translate(quote, src='en', dest='ru').text
        author = translator.translate(author, src='en', dest='ru').text
    else:
        quote = 'Ошибка при получении цитаты'
        author = ''
    return render_template('index.html', quote=quote, author=author)
