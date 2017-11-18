from models import User
from instagramApi import api
import peewee

from datetime import datetime, timedelta

users = User.select().where(User.mutual.is_null())
print(len(users))
for user in users:
    user.mutual = 0
    user.save()

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


