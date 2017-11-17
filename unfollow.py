from InstagramAPI import InstagramAPI
import json

with open('account.json', 'r') as f:
    account = json.loads(f.read())
    user, passwd = account['user'], account['passwd']
api = InstagramAPI(user, passwd)
api.login()
my_followings = api.getTotalSelfFollowings()
for user in my_followings['users'][:100]:
    api.unfollow(user['pk'])
print('Готово!!!')
