import allure

from api.petstore.petstore_api import (
    request_user_get,
    request_user_update,
)
from api.petstore.petstore_funcs import create_random_user
from api.petstore.petstore_models import User
from core.utils import (
    random_string,
    random_email,
    random_int32,
)


def test_update_user__no_new_values__user_is_same():
    with allure.step('Arrange:'):
        user = create_random_user()

    with allure.step('Act:'):
        response_update = request_user_update(username=user.username, updated_user=User())
        response_get = request_user_get(username=user.username)

    with allure.step('Assert:'):
        assert response_update.status_code == 200
        assert response_get.status_code == 200
        r = response_get.json()
        assert user.id == r['id']
        assert user.username == r['username']
        assert user.firstName == r['firstName']
        assert user.lastName == r['lastName']
        assert user.email == r['email']
        assert user.password == r['password']
        assert user.phone == r['phone']
        assert user.userStatus == r['userStatus']


def test_update_user__user_does_not_exist__404():
    # test will fail because if user doesn't exist, PUT method get 200 with userid = 0
    with allure.step('Arrange:'):
        username = random_string(50)

    with allure.step('Act:'):
        response = request_user_update(username=username, updated_user=User())

    with allure.step('Assert:'):
        assert response.status_code == 404


def test_update_user__all_new_values_except_id_and_username__values_updated():
    with allure.step('Arrange:'):
        user = create_random_user()
        updated_user = User(
            id=user.id,
            username=user.username,
            firstName=random_string(25),
            lastName=random_string(5),
            email=random_email(),
            password=random_string(60),
            phone=random_string(40),
            userStatus=random_int32()
        )

    with allure.step('Act:'):
        response_update = request_user_update(username=user.username, updated_user=updated_user)
        response_get = request_user_get(username=user.username)

    with allure.step('Assert:'):
        assert response_update.status_code == 200
        assert response_get.status_code == 200
        r = response_get.json()
        assert updated_user.id == r['id']
        assert updated_user.username == r['username']
        assert updated_user.firstName == r['firstName']
        assert updated_user.lastName == r['lastName']
        assert updated_user.email == r['email']
        assert updated_user.password == r['password']
        assert updated_user.phone == r['phone']
        assert updated_user.userStatus == r['userStatus']
