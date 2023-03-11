import sqlite3
from pathlib import Path


def db_init():
    """Для инициализации соединения с БД sqlite"""
    MAIN_PATH = Path(__file__).parent.parent
    DB_NAME = 'db_cars.sqlite'
    global db, cur
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cur = db.cursor()
    print("БД создана")


def create_table():
    """
    Создаем таблицу sqlite3
    """
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cars(
        model TEXT,
        price TEXT,
        mileage INTEGER,
        info TEXT
        )
        """
    )
    db.commit()


def done_cars():
    cur.execute(
        """
        SELECT * FROM  cars
        """
    )
    return cur.fetchall()


def get_cars(cars):
    """
    Заполнениние таблицы cars
    """
    db_init()
    cur.executemany("""INSERT INTO cars (
    model,
    price,
    mileage,
    info) VALUES (?, ?, ?, ?)""", cars)
    db.commit()


if __name__ == "__main__":
    db_init()
    create_table()
    done_cars()
