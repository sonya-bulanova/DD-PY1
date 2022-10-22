import string
import random

def get_random_password() -> str:
    str_set_randoms = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.sample(str_set_randoms, 8))
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
