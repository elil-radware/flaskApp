from app import create_app, db
from app.models.UsersModule import User




app = create_app('dev')
app.app_context().push()
db.drop_all()
db.create_all()
print("Flasky UP Using WSGI/GUnicorn")
# print(app.config.items())
User.create_user('admin', 'pass')
print("Flasky USER admin pass created")

print(User.get_all_users())