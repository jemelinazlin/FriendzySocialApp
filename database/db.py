import sqlite3

def create_users_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        ''')
        conn.commit()
        print('Table "users" created successfully.')
    except sqlite3.Error as e:
        print(f'Error creating table: {e}')

def create_posts_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                post_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            );
        ''')
        conn.commit()
        print('Table "posts" created successfully.')
    except sqlite3.Error as e:
        print(f'Error creating table: {e}')

def create_comments_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                post_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (post_id) REFERENCES posts (post_id)
            );
        ''')
        conn.commit()
        print('Table "comments" created successfully.')
    except sqlite3.Error as e:
        print(f'Error creating table: {e}')

if __name__ == '__main__':
    conn = sqlite3.connect('cli_social_media.db')
    create_users_table(conn)
    create_posts_table(conn)
    create_comments_table(conn)
    conn.close()
