import string
from randomuser import RandomUser
import random


def generate_random_user():
    """
    Generates random data for user creation
    :return: user_data dict
    """
    user = RandomUser()
    user_data = {
        'email': user.get_email(),
        'username': user.get_username(),
        'first_name': user.get_first_name(),
        'last_name': user.get_last_name(),
        'password': user.get_password()
    }
    return user_data


def generate_random_post():
    """
        Generates random data for post creation
        :return: post_data dict
    """
    post_data = {
        'title': ''.join(random.choice(string.ascii_letters) for i in range(15)),
        'text': ''.join(random.choice(string.ascii_letters) for i in range(150))
    }
    return post_data