from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        "caption": "Домашняя страница"
    }
    return render_template('home.html', **context)

@app.route('/blog')
def blog():
    context = {
        "caption": "Блог"
    }
    return render_template('blog.html', **context)

@app.route('/about')
def about():
    context = {
        "caption": " О создателях" }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run(debug=False)
