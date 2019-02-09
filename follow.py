import time
from datetime import datetime

import peewee

from models import User
from settings import api, REQUESTS_NUMBER, log, Timeout

COUNT = 0
users_for_following = []
api.login()
while True:
    target_account = input('Введите название аккаунта в Инстаграме [master_sporta19]: ')
    if not target_account:
        target_account = 'master_sporta19'
    try:
        api.searchUsername(target_account)
        target_account_id = api.LastJson['user']['pk']
        break
    except:
        print('Аккаунт не найден. Попробуйте еще раз.')
        continue
print(f'Получаем подписчиков аккаунта {target_account}')
followers = api.getTotalFollowers(target_account_id)
log(f'Получено {len(followers)} подписчиков аккаунта {target_account}')
log('Запуск процедуры подписки')
timeout = Timeout()
for follower in followers:
    try:
        User.get(User.uid == follower['pk'])
    except peewee.DoesNotExist:
        users_for_following.append(follower)
        if len(users_for_following) >= REQUESTS_NUMBER:
            break
if users_for_following:
    for count, user in enumerate(users_for_following, start=1):
        api.follow(user['pk'])
        if api.LastJson['status'] == 'fail':
            log(f'Ошибка при обращении к сервису Инстаграм: {api.LastJson["message"]}')
            break
        else:
            print(f'{count:3}    Подписываемся на {user["username"]}')
            User.create(uid=user['pk'],
                        username=user['username'],
                        full_name=user['full_name'],
                        following_date=datetime.now())
            COUNT = count
            time.sleep(timeout.follow)
else:
    print('Отсутствуют пользователи, на которых можно подписаться')
print()
print('=' * 80, '\n')
log(f'Отправлено новых заявок на подписку: {COUNT}')
input('\nДля выхода нажмите Enter...')
