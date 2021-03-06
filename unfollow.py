import time
from datetime import datetime, timedelta

from models import User
from settings import api, log, NUMBER_OF_DAYS_BEFORE_UNFOLLOW, REQUESTS_NUMBER, Timeout

UNFOLLOWING_DATE = datetime.now() - timedelta(days=NUMBER_OF_DAYS_BEFORE_UNFOLLOW)
COUNT = 0

api.login()
my_followers_ids = [follower['pk'] for follower in api.getTotalSelfFollowers()]

my_followings = User.select()\
    .where(User.following_date <= UNFOLLOWING_DATE)\
    .where(User.status == 1)\
    .limit(REQUESTS_NUMBER)
log('Запуск процедуры отписки')
if my_followings:
    timeout = Timeout()
    for count, user in enumerate(my_followings, start=1):
        api.unfollow(user.uid)
        if api.LastJson['status'] == 'fail':
            log(f'Ошибка при обращении к сервису Инстаграм: {api.LastJson["message"]}')
            break
        else:
            print(f'{count:3}   Отписываемся от {user.username}')
            user.unfollowing_date = datetime.now()
            user.status = 0
            if user.uid in my_followers_ids:
                user.mutual = 1
            user.save()
            COUNT = count
            time.sleep(timeout.unfollow)
    print()
    print('=' * 80, '\n')
    log(f'Завершена отписка от {COUNT} человек')
else:
    print('=' * 80, '\n')
    log(f'Отсутствуют подписки старше {NUMBER_OF_DAYS_BEFORE_UNFOLLOW} дней')
input('\nДля выхода нажмите Enter...')
