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


class Timeout:
    base_follow_timeout = 30
    base_unfollow_timeout = 12

    @property
    def follow(self):  # Таймаут для подписки
        random_time = random.randint(0, 15)
        return self.base_follow_timeout + random_time

    @property
    def unfollow(self):  # Таймаут для отписки
        random_time = random.randint(0, 15)
        return self.base_unfollow_timeout + random_time


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SqliteExtDatabase(os.path.join(BASE_DIR, DB_FILE_NAME))
logfile = os.path.join(BASE_DIR, LOG_FILE_NAME)

api = InstagramAPI(user, passwd)


def log(message):
    with open(logfile, 'a', encoding='utf8') as f:
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(message)
        f.write(f'{date}    {message}\n')
