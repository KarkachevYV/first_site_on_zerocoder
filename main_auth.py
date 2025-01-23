from app_auth import db, app_auth

if __name__ == '__main__':
    # with app_auth.app_context():  # эти 2 строчки необходимы для создания таблицы базы данных без чего код всего приложения не будет работать, раскоментировать при первом запуске программы
    #     db.create_all()
    app_auth.run(debug=False)