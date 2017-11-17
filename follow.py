from InstagramAPI import InstagramAPI
import time
import json
from models import User
import peewee
from datetime import datetime


def read_db():
    with open('UsersDB.json', 'r', encoding='utf8') as f:
        return json.loads(f.read())


def main():
    with open('account.json', 'r') as f:
        account = json.loads(f.read())
        user, passwd = account['user'], account['passwd']
    api = InstagramAPI(user, passwd)
    api.login()
    while True:
        user_for_scan = input('Введи название паблика: ')
        try:
            api.searchUsername(user_for_scan)
            user_id_for_scan = api.LastJson['user']['pk']
            break
        except:
            print('Паблик не найден. Попробуй еще раз.')
            continue

    followers = api.getTotalFollowers(user_id_for_scan)
    users_for_following= []
    for follower in followers:
        try:
            User.get(User.uid == follower['pk'])
        except peewee.DoesNotExist:
            users_for_following.append(follower)
            if len(users_for_following) >= 100:
                for user in users_for_following:
                    api.follow(user['pk'])
                    User.create(uid=user['pk'],
                                username=user['username'],
                                full_name=user['full_name'],
                                following_date=datetime.now(),
                                status=1)
                break

    print(f'Отправлено новых заявок на подписку: {len(users_for_following)}')
    time.sleep(5)

if __name__ == '__main__':
    main()