from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3cdd92a0fee3b4c2747bba061eaefc8c'

from app import routes