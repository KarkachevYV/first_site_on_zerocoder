from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    title = request.form.get('title')
    content = request.form.get('content')
    if name and age and city and content:
      posts.append({'name': name, 'age': age, 'city': city, 'title': title, 'content': content})
      return redirect(url_for('index'))
  return render_template('blog.html', posts=posts)  