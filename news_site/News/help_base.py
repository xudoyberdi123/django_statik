from sqlite3 import connect
con = connect("../db.sqlite3")
cur = con.cursor()

def search(search):
    var = cur.execute(""" SELECT * FROM news_news """)

    print(cur.fetchall())

