import sqlite3
from sqlite3 import Error


def create_connection(db_file, persistent_path):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(persistent_path + '/' + db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Db created successfully")
            conn.close()


if __name__ == '__main__':
    create_connection("sqlite.db")
