from api.petstore.petstore_models import User
from core.request import make_request

# swagger — https://petstore.swagger.io/#/user
BASE_URL = 'https://petstore.swagger.io/'


def request_user_create(user: User):
    body = user.get_user()
    response = make_request(method='POST', url=BASE_URL+'v2/user', json=body)
    if user.id is None:
        response_json = response.json()
        user.id = int(response_json['message'])
    return response


def request_user_get(username: str):
    response = make_request(method='GET', url=BASE_URL + f'v2/user/{username}')
    return response


def request_user_update(user: User):
    pass


def request_user_delete(user: User):
    pass
