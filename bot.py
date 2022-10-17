from bot.main import Bot


if __name__ == '__main__':
    bot = Bot()
    bot.register_users()
    bot.create_posts()
    bot.like_posts()