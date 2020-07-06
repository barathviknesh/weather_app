import sqlite3

db_name = 'database.db'


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("try works from db")
        return conn
    except Exception as e:
        print(e)
        return None


def create_table():
    cons = sqlite3.connect(db_name)
    c = cons.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS news (
                                         location text,
                                        temperature text,
                                        description text
             )""")
    print("table created")


create_connection(db_name)
print("from db end")
create_table()
print(" ACK final table created")
