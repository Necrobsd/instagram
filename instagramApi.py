from InstagramAPI import InstagramAPI
import json


with open('account.json', 'r') as f:
    account = json.loads(f.read())
    user, passwd = account['user'], account['passwd']
api = InstagramAPI(user, passwd)
