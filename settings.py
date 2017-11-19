from InstagramAPI import InstagramAPI
from playhouse.sqlite_ext import SqliteExtDatabase
from datetime import datetime
import json
import os


LOG_FILE_NAME = 'instagram.log'
DB_FILE_NAME = 'Users.sqlite3'
NUMBER_OF_DAYS_BEFORE_UNFOLLOW = 5  # Количество дней до начала отписки
REQUESTS_NUMBER = 100  # Количество обращений к АПИ Инстаграм за один запуск


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SqliteExtDatabase(os.path.join(BASE_DIR, DB_FILE_NAME))
logfile = os.path.join(BASE_DIR, LOG_FILE_NAME)

with open('account.json', 'r') as f:
    account = json.loads(f.read())
    user, passwd = account['user'], account['passwd']
api = InstagramAPI(user, passwd)


def log(message):
    with open(logfile, 'a', encoding='utf8') as f:
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(message)
        f.write(f'{date}    {message}\n')
