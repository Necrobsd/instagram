from instagramApi import api
from models import User
from datetime import datetime, timedelta
import time


NUMBER_OF_DAYS_BEFORE_UNFOLLOW = 5
FIVE_DAYS_AGO = datetime.now() - timedelta(days=NUMBER_OF_DAYS_BEFORE_UNFOLLOW)
REQUESTS_NUMBER = 100
api.login()
my_followers_ids = [follower['pk'] for follower in api.getTotalSelfFollowers()]

my_followings = User.select()\
    .where(User.following_date <= FIVE_DAYS_AGO)\
    .where(User.status == 1)\
    .order_by(User.id).limit(REQUESTS_NUMBER)
if my_followings:
    for count, user in enumerate(my_followings, start=1):
        api.unfollow(user.uid)
        print(f'{count:3}   Отписываемся от {user.username}')
        user.unfollowing_date = datetime.now()
        user.status = 0
        if user.uid in my_followers_ids:
            user.mutual = 1
        user.save()
    print(f'Завершена отписка от {REQUESTS_NUMBER} человек')
else:
    print(f'Отсутствуют подписки старше {NUMBER_OF_DAYS_BEFORE_UNFOLLOW} дней')
time.sleep(5)
