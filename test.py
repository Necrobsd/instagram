from models import User
import json
from InstagramAPI import InstagramAPI
from datetime import datetime


with open('account.json', 'r') as f:
    account = json.loads(f.read())
    user, passwd = account['user'], account['passwd']
api = InstagramAPI(user, passwd)
api.login()

with open('UsersDB.json', 'r', encoding='utf8') as f:
    user_ids = json.loads(f.read())[800:900]
for count, uid in enumerate(user_ids, start=1):
    print(count, '    uid=', uid)
    api.getUsernameInfo(uid)
    if 'user' in api.LastJson:
        try:
            user = User.create(uid=uid,
                               username=api.LastJson['user']['username'],
                               full_name=api.LastJson['user']['full_name'],
                               following_date=datetime(2017, 11, 10, 00, 00, 0, 000000),
                               status=1)
        except:
            print('Пользователь уже в базе')
            pass
    else:
        print('Получена ошибка: {}'.format(api.LastJson['message']))
        break


# my_followings = [user['pk'] for user in api.getTotalSelfFollowings()]
# users = User.select().where(User.status == 1)
# for user in users:
#     if user.uid not in my_followings:
#         user.unfollowing_date = datetime.now()
#         user.status = 0
#         user.save()
