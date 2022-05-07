import sqlite3


def createMenu():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        create_table_query = '''CREATE TABLE IF NOT EXISTS menu (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL
                                );'''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectMenu():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM menu;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for record in records:
            print(record[1])

        cursor.close()

    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def insertManyDataMenu(id, name):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        insert_data_query = '''INSERT INTO menu (id, name)
                               VALUES (?, ?);'''

        cursor.execute(insert_data_query, (id, name))
        sqlite_connection.commit()
        print("Запись успешно добавлена.")
        cursor.close()

    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def lastID():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT MAX(id) FROM menu;"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchone()
        cursor.close()
        return record[0]
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()