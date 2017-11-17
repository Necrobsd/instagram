from InstagramAPI import InstagramAPI
import time
import json


def read_db():
    with open('UsersDB.json', 'r', encoding='utf8') as f:
        return json.loads(f.read())


def main():
    with open('account.json', 'r') as f:
        account = json.loads(f.read())
        user, passwd = account['user'], account['passwd']
    api = InstagramAPI(user, passwd)
    api.login()
    old_users_ids = set(read_db())
    print(f'Ранее было отправлено заявок на подписку: {len(old_users_ids)}')
    current_followings_ids = {user['pk'] for user in api.getTotalSelfFollowings()}
    print(f'На текущий момент Вы подписаны на {len(current_followings_ids)} человек')
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
    users_ids_for_following = []
    for follower in followers:
        if follower['pk'] not in old_users_ids:
            users_ids_for_following.append(follower['pk'])
            if len(users_ids_for_following) >= 100:
                for user_id_for_scan in users_ids_for_following:
                    api.follow(user_id_for_scan)
                    old_users_ids.add(user_id_for_scan)
                break
    with open('UsersDB.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(list(old_users_ids)))
    print(f'Отправлено новых заявок на подписку: {len(users_ids_for_following)}')
    time.sleep(5)
    print('Готово!!!')

if __name__ == '__main__':
    main()