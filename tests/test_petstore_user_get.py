import allure

from api.petstore.petstore_api import request_user_get, request_user_create
from api.petstore.petstore_funcs import create_random_user
from core.utils import random_string


def test_get_user__user_ixists__fields_are_same_as_on_creation__200():
    with allure.step('Arrange:'):
        user = create_random_user()
        request_user_create(user=user)

    with allure.step('Act:'):
        response = request_user_get(username=user.username)

    with allure.step('Assert:'):
        assert response.status_code == 200
        r = response.json()
        assert user.id == r['id']
        assert user.username == r['username']
        assert user.firstName == r['firstName']
        assert user.lastName == r['lastName']
        assert user.email == r['email']
        assert user.password == r['password']
        assert user.phone == r['phone']
        assert user.userStatus == r['userStatus']


def test_get_user__user_does_not_exist__404():
    with allure.step('Arrange:'):
        username = random_string(50)

    with allure.step('Act:'):
        response = request_user_get(username=username)

    with allure.step('Assert:'):
        assert response.status_code == 404
