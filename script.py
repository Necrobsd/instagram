from models import User
from instagramApi import api
import peewee, time

from datetime import datetime, timedelta

users = User.select().limit(150)
print(len(users))
for count, user in enumerate(users):
    print(f'{count:3} Пользователь {user.username} в базе!')
time.sleep(5)
#
# api.login()
# my_followers = api.getTotalSelfFollowers()
# for follower in my_followers:
#     try:
#         user = User.get(User.uid == follower['pk'])
#         # user.mutual = 1
#         # user.save()
#         # print('Сохранен', user.username)
#     except peewee.DoesNotExist:
#         print('Пользователь отсутствует в базе данных')
#         User.create(uid=follower['pk'],
#                     username=follower['username'],
#                     full_name=follower['full_name'],
#                     following_date=datetime.now() - timedelta(days=15)
#                     )


