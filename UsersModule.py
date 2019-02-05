from settings import db
# from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def username_password_match(_usernamae, _password):
        user = User.query.filter_by(username=_usernamae).filter_by(password=_password).first()
        if user is None:
            return False
        else:
            return True

    def get_all_users():
        return User.query.all()


    def create_user( _username, _password):
        new_user = User(username=_username, password=_password)
        db.session.add(new_user)
        db.session.commit()

    def __repr__(self):
        user_obj = {
            'username': self.username,
            'password': self.password
        }
        return str(user_obj)

