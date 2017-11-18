from models import User
from instagramApi import api

from datetime import datetime



# api.login()

# with open('UsersDB.json', 'r', encoding='utf8') as f:
#     user_ids = json.loads(f.read())
my_followings = api.getTotalSelfFollowings()
users_in_db = [u.uid for u in User.select()]
for following in my_followings:
    if following['pk'] not in users_in_db:
        print('Добавлям юзера: ', following['username'])
        # api.getUsernameInfo(following)
        # if 'user' in api.LastJson:
        #     try:
        user = User.create(uid=following['pk'],
                           username=following['username'],
                           full_name=following['full_name'],
                           following_date=datetime.now()
                           )
            # except:
            #     print('Пользователь уже в базе')
        # else:
        #     print('Получена ошибка: {}'.format(api.LastJson['message']))
        #     break



# users = User.select().where(User.status == 1)
# for user in users:
#     if user.uid not in my_followings:
#         user.unfollowing_date = datetime.now()
#         user.status = 0
#         user.save()
