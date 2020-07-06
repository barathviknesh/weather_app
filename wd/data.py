import sqlite3

conn = sqlite3.connect('report.db')
# create cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE customer (
        place text,
        status text,
        temperature text
)""")


def add_w(location, s, t):
    # connect to database
    conn = sqlite3.connect('record.db')
    # create cursor
    c = conn.cursor()
    # query
    c.execute("INSERT INTO customer VALUES (?,?,?)", (location, s, t))
    # print
    print("from addone")
    # commited command
    conn.commit()
    # close our connection
    conn.close()


print("it works")
# commited command
# conn.commit()
# close our connection
# conn.close()
