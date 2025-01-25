#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app_api = Flask(__name__)

#формируем путь и методы GET и POST
@app_api.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
   weather = None
   news = None
#формируем условия для проверки метода. Форму мы пока не создавали, но нам из неё необходимо будет взять только город.   
   if request.method == 'POST':
       news = get_news()
#этот определенный город мы будем брать для запроса API
       city = request.form['city']
       #прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
       weather = get_weather(city)
       
       #передаем информацию о погоде и  информацию о новорстях в index.html
   return render_template("index.html", news=news, weather=weather)

#в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
   api_key = "f59d92d7531d3b3597d79873278fa83a"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

def get_news():
   api_key = "46628fae24f5475db9de67e4fdebfceb"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])