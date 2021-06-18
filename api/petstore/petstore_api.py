import allure

from api.petstore.petstore_models import User
from core import settings
from core.request import make_request
import time

# swagger — https://petstore.swagger.io/#/user
BASE_URL = 'https://petstore.swagger.io/'


def request_user_create(user: User):
    body = user.get_user()
    response = make_request(method='POST', url=BASE_URL+'v2/user', json=body)
    if user.id is None:
        response_json = response.json()
        user.id = int(response_json['message'])
    with allure.step('Waiting for changes after user was created'):
        time.sleep(settings.WAIT_TIME)
    return response


def request_user_get(username: str):
    response = make_request(method='GET', url=BASE_URL + f'v2/user/{username}')
    return response


def request_user_update(username: str, updated_user: User):
    body = updated_user.get_user()
    response = make_request(method='PUT', url=BASE_URL + f'v2/user/{username}', json=body)
    with allure.step('Waiting for changes after user was updated'):
        time.sleep(settings.WAIT_TIME)
    return response


def request_user_delete(username: str):
    response = make_request(method='DELETE', url=BASE_URL + f'v2/user/{username}')
    with allure.step('Waiting for changes after user was deleted'):
        time.sleep(settings.WAIT_TIME)
    return response
