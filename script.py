from models import User
from settings import api
import peewee, time


api.login()
users = User.select().order_by(User.id.desc()).limit(200)
print(len(users))
for count, user in enumerate(users, 1):
    api.follow(user.uid)
    print(f'Подписка на {user.username}')
    print(api.LastJson)




