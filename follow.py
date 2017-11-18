from instagramApi import api
import time
from models import User
import peewee
from datetime import datetime


COUNT_REQUESTS = 100
users_for_following = []
api.login()
while True:
    target_account = input('Введи название паблика: ')
    try:
        api.searchUsername(target_account)
        target_account_id = api.LastJson['user']['pk']
        break
    except:
        print('Паблик не найден. Попробуй еще раз.')
        continue

followers = api.getTotalFollowers(target_account_id)
for follower in followers:
    try:
        User.get(User.uid == follower['pk'])
    except peewee.DoesNotExist:
        users_for_following.append(follower)
        if len(users_for_following) >= COUNT_REQUESTS:
            break
for user in users_for_following:
    api.follow(user['pk'])
    print(f'Подписываемся на {user["username"]}')
    User.create(uid=user['pk'],
                username=user['username'],
                full_name=user['full_name'],
                following_date=datetime.now())

print(f'Отправлено новых заявок на подписку: {len(users_for_following)}')
time.sleep(5)
