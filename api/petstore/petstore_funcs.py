from api.petstore.petstore_api import request_user_create
from api.petstore.petstore_models import User
from core.utils import (
    random_string,
    random_email,
    random_int32,
)


def create_random_user() -> User:
    user = User(
        username=random_string(20),
        firstName=random_string(),
        lastName=random_string(),
        email=random_email(),
        password=random_string(),
        phone=random_string(),
        userStatus=random_int32()
    )
    request_user_create(user=user)
    return user
