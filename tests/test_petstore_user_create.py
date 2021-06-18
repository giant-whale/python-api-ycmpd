import allure

from api.petstore.petstore_api import request_user_create
from api.petstore.petstore_models import User
from core.utils import (
    random_int32,
    random_string,
    random_email,
)


def test_create_user__id_only__200():
    with allure.step('Arrange:'):
        user = User(
            id=random_int32()
        )

    with allure.step('Act:'):
        response = request_user_create(user=user)

    with allure.step('Assert:'):
        assert response.status_code == 200


def test_create_user__all_parameters__200():
    with allure.step('Arrange:'):
        user = User(
            id=random_int32(),
            username=random_string(20),
            firstName=random_string(),
            lastName=random_string(),
            email=random_email(),
            password=random_string(),
            phone=random_string(),
            userStatus=random_int32()
        )

    with allure.step('Act:'):
        response = request_user_create(user=user)

    with allure.step('Assert:'):
        assert response.status_code == 200


def test_create_user__id_type__500():
    with allure.step('Arrange:'):
        user = User(
            id=random_string()
        )

    with allure.step('Act:'):
        response = request_user_create(user=user)

    with allure.step('Assert:'):
        assert response.status_code == 500
