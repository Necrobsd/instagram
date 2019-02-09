import os
import random
from datetime import datetime

from InstagramAPI import InstagramAPI
from playhouse.sqlite_ext import SqliteExtDatabase

from account import user, passwd

LOG_FILE_NAME = 'instagram.log'
DB_FILE_NAME = 'Users.sqlite3'
NUMBER_OF_DAYS_BEFORE_UNFOLLOW = 5  # Количество дней до начала отписки
REQUESTS_NUMBER = 100  # Количество обращений к АПИ Инстаграм за один запуск


def follow_timeout():  # Таймаут для подписки
    base_time = 30
    random_time = random.randint(0, 15)
    return base_time + random_time


def unfollow_timeout():  # Таймаут для отписки
    base_time = 12
    random_time = random.randint(0, 15)
    return base_time + random_time


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SqliteExtDatabase(os.path.join(BASE_DIR, DB_FILE_NAME))
logfile = os.path.join(BASE_DIR, LOG_FILE_NAME)

api = InstagramAPI(user, passwd)


def log(message):
    with open(logfile, 'a', encoding='utf8') as f:
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(message)
        f.write(f'{date}    {message}\n')
