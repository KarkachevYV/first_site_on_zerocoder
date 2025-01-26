from app_site import app, db
from app_site.models import User

# with app.app_context(): # После первого запуска эту строку можно удалить
#     db.create_all() # После первого запуска эту строку можно удалить
    
if __name__ == '__main__':
    app.run(debug=False)

