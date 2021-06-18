import allure

from api.petstore.petstore_api import (
    request_user_get,
    request_user_delete,
)
from api.petstore.petstore_funcs import create_random_user
from core.utils import random_string


def test_delete_user__user_exists__200_delete_404_get():
    with allure.step('Arrange:'):
        user = create_random_user()

    with allure.step('Act:'):
        response_delete = request_user_delete(username=user.username)
        response_get = request_user_get(username=user.username)

    with allure.step('Assert:'):
        assert response_delete.status_code == 200
        assert response_get.status_code == 404


def test_delete_user__user_does_not_exist__404():
    with allure.step('Arrange:'):
        username = random_string(50)

    with allure.step('Act:'):
        response = request_user_delete(username=username)

    with allure.step('Assert:'):
        assert response.status_code == 404
