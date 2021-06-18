# swagger — https://petstore.swagger.io/#/user

class User:
    def __init__(
            self,
            id: int = None,
            username: str = None,
            firstName: str = None,
            lastName: str = None,
            email: str = None,
            password: str = None,
            phone: str = None,
            userStatus: int = None
    ):
        """
        :param id: int64, do not fill to generate new; must be unique
        :param username: must be unique
        :param userStatus: int32
        """
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    def get_user(self) -> dict:
        return self.__dict__
