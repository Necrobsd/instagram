from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime
import os
import time
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SqliteExtDatabase(os.path.join(BASE_DIR, 'Users.sqlite3'))


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    uid = IntegerField(index=True, unique=True)
    username = CharField(max_length=255)
    full_name = CharField(max_length=255)
    following_date = DateTimeField(default=datetime.datetime.now, verbose_name='Дата подписки')
    unfollowing_date = DateTimeField(null=True, verbose_name='Дата отписки')
    status = BooleanField(index=True, default=1, verbose_name='Статус подписки')


db.connect()
if not User.table_exists():
    print("В базе отсутствуют таблицы с данными")
    while True:
        answer = input("Создать новые таблицы? [y/n]: ")
        if answer.lower() == 'y':
            db.create_table(User)
            break
        elif answer.lower() == 'n':
            sys.exit(0)
        else:
            print("Введен неверный ответ")
