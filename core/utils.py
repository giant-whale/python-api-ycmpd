import random
import string


def random_string(length=10) -> str:
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def random_email(user_length=6, domain_length=10, domain_zone_length=2) -> str:
    return random_string(user_length) + '@' + random_string(domain_length) + '.' + random_string(domain_zone_length)


def random_int32() -> int:
    return random.randint(0, 2147483648)
