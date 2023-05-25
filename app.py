import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()

response = {'Answer': 'Which response server'}

fake_database = {'users': [
    {
        "id": 1,             # тут тип данных - число
        "name": "Anna",      # тут строка
        "nick": "Anny42",    # и тут
        "balance": 15.01    # а тут float
     },

    {
        "id": 2,             # у второго пользователя
        "name": "Dima",      # такие же
        "nick": "dimon2319", # типы
        "balance": 8.01     # данных
     },
    {
        "id": 3,             # у третьего
        "name": "Vladimir",  # юзера
        "nick": "Vova777",   # мы специально сделаем
        "balance": "23"     # нестандартный тип данных в его балансе
     }
],
}


@api.get('/')
def index():
    return response


@api.get('/static/path')
def hello():
    return 'hello'


@api.get('/about/us')
def about():
    return {'We are': 'Legion'}


@api.get('/user/{nick}')
def get_nick(nick):
    return {'user': nick}


@api.get('/userid/{id1:int}')
def get_id(id1):
    return {'user': id1}


@api.get('/user_id/{id2}')
def get_id2(id2: int):
    return {'user': id2}


@api.get('/test/{id3:int}/{text:str}/{custom_path:path}')
def get_test(id3, text, custom_path):
    return {'id': id3, 'text': text, 'custom_path': custom_path}
