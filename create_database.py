import sqlite3

dbname = 'main.db'

def create_database():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        cur.execute(
            "CREATE TABLE items(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, created TIMESTAMP DATETIME DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')))"
        )
    except:
        print("データベースはすでに作成されています")
    conn.close()

create_database()