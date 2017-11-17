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
    user_ids = json.loads(f.read())[199:300]
for count, uid in enumerate(user_ids):
    print(count, '    uid=', uid)
    api.getUsernameInfo(uid)
    user = User.create(uid=uid,
                       username=api.LastJson['user']['username'],
                       full_name=api.LastJson['user']['full_name'],
                       following_date=datetime(2017, 11, 10, 00, 00, 0, 000000),
                       status=1)
