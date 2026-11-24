import psycopg2


def create_connection():
    conn = psycopg2.connect(
        dbname="register_login",
        host="localhost",
        port=5432,
        user="postgres",
        password="adminadmin",
    )
    return conn


def init_db():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255)
        )
        """
    )
    conn.commit()
    cursor.close()
    conn.close()


def check_user_exists(email, username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT email, username FROM users WHERE LOWER(email) = LOWER(%s) OR LOWER(username) = LOWER(%s)",
        (email, username),
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def register_user(email, hashed_password, username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (email, password, username) VALUES (%s, %s, %s)",
        (email, hashed_password, username),
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_user_by_email(email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, email, password FROM users WHERE LOWER(email) = LOWER(%s)",
        (email,),
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def update_user_password(email, new_hashed_password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET password = %s WHERE LOWER(email) = LOWER(%s)",
        (new_hashed_password, email),
    )
    conn.commit()
    cursor.close()
    conn.close()


def delete_user_by_email(email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM users WHERE LOWER(email) = LOWER(%s)",
        (email,),
    )
    conn.commit()
    cursor.close()
    conn.close()
