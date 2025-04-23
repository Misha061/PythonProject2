from db import get_connection
from validators import is_valid_email, is_strong_password


def register_user(email, password):
    if not is_valid_email(email):
        return "Неправильний формат email"
    if not is_strong_password(password):
        return "Пароль занадто простий"

    conn = get_connection()
    if not conn:
        return "Проблема з підключенням до БД"

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        return "Користувача зареєстровано"
    except Exception as e:
        return f"Реєстрація не вдалася: {str(e)}"
    finally:
        conn.close()


def authenticate(email, password):
    conn = get_connection()
    if not conn:
        return "Проблема з підключенням до БД"

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return "Вхід успішний"
    else:
        return "Невірний логін або пароль"
