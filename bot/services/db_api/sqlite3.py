import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('bot.db')
        self.create_db_if_not_exists()

    def __del__(self):
        # closing connection when object destroyed
        self.conn.close()

    def create_db_if_not_exists(self):
        self.conn.execute(
            '''CREATE TABLE IF NOT EXISTS USERS
                 (
                 EMAIL           CHAR(255)    NOT NULL,
                 PASSWORD        CHAR(255)    NOT NULL
                 );'''
        )

    def insert_user(self, email: str, password: str):
        self.conn.execute("INSERT INTO USERS (EMAIL,PASSWORD) \
              VALUES ($e, $p)", {'e': email, 'p': password})
        self.conn.commit()

    def select_all_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM USERS")

        rows = cur.fetchall()
        return rows
