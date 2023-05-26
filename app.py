import fastapi
import database
import pydantic_models
import config
from typing import Optional

api = fastapi.FastAPI()

response = {'Answer': 'Which response server'}

fake_database = {
    'users': [
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


fake_database_2 = {
    'users': [
        {
            "id": 1,             # тут тип данных - число
            "name": "Anna",      # тут строка
            "nick": "Anny42",    # и тут
            "balance": 15300    # а тут int
         },

        {
            "id": 2,             # у второго пользователя
            "name": "Dima",      # такие же
            "nick": "dimon2319", # типы
            "balance": 160.23     # float
         },
        {
            "id": 3,             # у третьего
            "name": "Vladimir",  # юзера
            "nick": "Vova777",   # мы специально сделаем
            "balance": "25000"     # нестандартный тип данных в его балансе
        }
    ],
}

@api.get('/')
def index():
    return response


@api.get('/static/path', tags=['first_test_endpoints'])
def hello():
    return 'hello'


@api.get('/about/us', tags=['first_test_endpoints'])
def about():
    return {'We are': 'Legion'}


@api.get('/user/{nick}', tags=['first_test_endpoints'])
def get_nick(nick):
    return {'user': nick}


@api.get('/userid/{id1:int}', tags=['first_test_endpoints'])
def get_id(id1):
    return {'user': id1}


@api.get('/user_id/{id2}', tags=['first_test_endpoints'])
def get_id2(id2: int):
    return {'user': id2}


@api.get('/test/{id3:int}/{text:str}/{custom_path:path}', tags=['first_test_endpoints'])
def get_test(id3, text, custom_path):
    return {'id': id3, 'text': text, 'custom_path': custom_path}


@api.get('/get_info_by_user_id/{user_id:int}', tags=['user_info'])
def get_info_by_user_id(user_id):
    return fake_database['users'][user_id - 1]


@api.get('/get_user_balance_by_id/{user_id:int}', tags=['user_info'])
def get_user_balance_by_id(user_id):
    return fake_database['users'][user_id - 1]['balance']


@api.get('/get_total_balance', tags=['user_info'])
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database_2['users']:
        total_balance += pydantic_models.User(**user).balance
    return total_balance


@api.get('/users')
def get_users(skip: int, limit: int):
    return fake_database['users'][skip: skip + limit]


@api.get('/user/{user_id}')
def get_user(user_id: str, query: Optional[str] = None):
    if query is not None:
        return {'user_id': user_id, 'query': query}
    return {'user_id': user_id}
