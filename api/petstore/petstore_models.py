# swagger — https://petstore.swagger.io/#/user

class User:
    id = int
    """Do not use to generate new ID"""
    username = str
    firstName = str
    lastName = str
    email = str
    password = str
    phone = str
    userStatus = int

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
