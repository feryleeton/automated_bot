import random

import requests

import config
from bot.services.db_api.sqlite3 import Database
from bot.services import helper_funcs


def send_creation_user_request():
    """
    Sends request to create new user, with generated random data
    :return: email, password - creds for saving user in bot`s database
    """
    user_data = helper_funcs.generate_random_user()
    requests.post('http://127.0.0.1:8000/accounts/register/', json=user_data)
    return user_data.get('email'), user_data.get('password')


def send_creation_post_request(access_token):
    post_data = helper_funcs.generate_random_post()
    headers = {
        "Authorization": "Bearer %s" % (access_token, ),
    }
    requests.post('http://127.0.0.1:8000/feed/posts/', json=post_data, headers=headers)


def send_like_post_request(access_token, post_pk):
    headers = {
        "Authorization": "Bearer %s" % (access_token,),
    }
    requests.post('http://127.0.0.1:8000/feed/posts/like/%d' % post_pk, headers=headers)


def get_all_posts():
    """
    Sends request to collect all posts, going throw pagination
    :return: posts - list of posts received
    """
    url = 'http://127.0.0.1:8000/feed/posts'
    posts = []
    response = requests.get(url).json()
    while True:
        for post in response.get('results'):
            posts.append(post)
        if response.get('next'):
            url = response.get('next')
            response = requests.get(url).json()
        else:
            break
    return posts


def authenticate_user(user):
    """
    Authenticates user by given creds
    :param user: user data
    :return: JWT access_token
    """
    login_data = {
        'email': user[0],
        'password': user[1],
    }
    response = requests.post('http://127.0.0.1:8000/accounts/token/', json=login_data)
    access_token = response.json()['access']
    return access_token


class Bot:
    def __init__(self):
        self.db = Database()

    def register_users(self):
        for counter in range(config.NUMBER_OF_USERS):
            email, password = send_creation_user_request()
            self.db.insert_user(email, password)

    def create_posts(self):
        users = self.db.select_all_users()
        for user in users:
            access_token = authenticate_user(user)
            for counter in range(random.randrange(0, config.MAX_POSTS_PER_USER)):
                send_creation_post_request(access_token)

    def like_posts(self):
        users = self.db.select_all_users()
        posts = get_all_posts()
        for user in users:
            for counter in range(random.randrange(0, config.MAX_LIKES_PER_USER)):
                access_token = authenticate_user(user)
                post_pk = random.choice(posts).get('id')
                send_like_post_request(access_token, post_pk)