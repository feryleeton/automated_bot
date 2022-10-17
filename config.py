import environ

env = environ.Env()
environ.Env.read_env()

NUMBER_OF_USERS = int(env('NUMBER_OF_USERS'))
MAX_POSTS_PER_USER = int(env('MAX_POSTS_PER_USER'))
MAX_LIKES_PER_USER = int(env('MAX_LIKES_PER_USER'))
