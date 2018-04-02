from models import User
from settings import api
import peewee, time
from InstagramAPI import InstagramAPI


api = InstagramAPI('', '')
api.login()
TIMEOUT = 10  # Таймаут между обращениями к АПИ (секунд)
likers_ids = set()  # id пользователей, которые поставили хотя бы один лайк
commentators_ids = set()  # id пользователей, которые оставили хотя бы один коммент
media_with_comments = set()
media_with_likes = set()

more_available = True
maxid = None
i = 1
while more_available:
    print('итерация ', i)
    api.getUserFeed(6091081871, maxid=maxid)
    i += 1
    more_available = api.LastJson.get('more_available', False)
    if more_available:
        maxid = api.LastJson.get('next_max_id')
    media = api.LastJson.get('items', None)
    for item in media:
        if item['comment_count']:
            print('добавляем медиа с комментариями')
            media_with_comments.add(item['id'])
        if item['like_count']:
            if item['like_count'] <= 10:
                for liker in item['likers']:
                    print('добавляем лайкера')
                    likers_ids.add(liker['pk'])
            elif item['like_count'] > 10:
                print('добавляем медиа с лайками. item id=', item['id'])
                media_with_likes.add(item['id'])
    print(f'Спим {TIMEOUT} секунд')
    time.sleep(TIMEOUT)


for media_id in media_with_comments:
    has_more_comments = True
    max_id = ''
    while has_more_comments:
        api.getMediaComments(media_id, max_id=max_id)
        # comments' page come from older to newer, lets preserve desc order in full list
        for c in api.LastJson['comments']:
            print('media id=', media_id)
            print(f"{c['user']['full_name']}: {c['text']}")
            commentators_ids.add(c['user_id'])
        has_more_comments = api.LastJson.get('has_more_comments', False)
        if has_more_comments:
            max_id = api.LastJson.get('next_max_id', '')
            print('Спим 2 секунды')
            time.sleep(2)
    print('Спим 5 секунд')
    time.sleep(5)
