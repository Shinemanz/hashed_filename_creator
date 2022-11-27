import sqlite3

dbname = 'main.db'

def insert_item():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name) values('dummy')")
    conn.commit()
    conn.close()

def fetch_item():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM items ORDER BY created DESC LIMIT 1')
    val = 0
    for row in cur:
        val = str(row[0])
    conn.close()    
    return val