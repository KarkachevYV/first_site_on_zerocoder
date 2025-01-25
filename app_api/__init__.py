from flask import Flask, render_template, request, jsonify
import requests
from googletrans import Translator

app_api = Flask(__name__)

@app_api.route('/')
def home():
    return render_template("index.html")

@app_api.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather = get_weather(city)
    translated_weather = translate_text(weather['weather'][0]['description'])
    weather['weather'][0]['description'] = translated_weather
    return jsonify(weather=weather)

@app_api.route('/news', methods=['GET'])
def news():
    news = get_news()
    translated_news = [{'title': translate_text(article['title']), 'url': article['url']} for article in news]
    return jsonify(news=translated_news)

def get_weather(city):
    api_key = "f59d92d7531d3b3597d79873278fa83a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "46628fae24f5475db9de67e4fdebfceb"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])

def translate_text(text, lang='ru'):
    translator = Translator()
    translated = translator.translate(text, dest=lang)
    return translated.text