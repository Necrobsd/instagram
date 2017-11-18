from instagramApi import api
from models import User
from datetime import datetime, timedelta
import time


FIVE_DAYS_AGO = datetime.now() - timedelta(days=5)
COUNT_REQUESTS = 100
api.login()
my_followings = User.select()\
    .where(User.following_date <= FIVE_DAYS_AGO)\
    .where(User.status == 1).order_by(User.id)
for user in my_followings[:COUNT_REQUESTS]:
    api.unfollow(user.uid)
    print(f'Отписываемся от {user.uid}')
    user.unfollowing_date = datetime.now()
    user.status = 0
    user.save()
print(f'Завершена отписка от {COUNT_REQUESTS} человек')
time.sleep(5)