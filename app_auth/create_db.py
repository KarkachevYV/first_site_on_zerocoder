from app_auth import db, app_auth
from app_auth.models import User

with app_auth.app_context():
    db.create_all()
