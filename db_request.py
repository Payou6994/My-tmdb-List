import sqlite3
import json


def get_data(db, tmdb_id):
    con = sqlite3.connect("Mylist.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"SELECT * FROM {db} WHERE tmdb_id = {int(tmdb_id)};").fetchall()
    con.commit()
    con.close()
    result = json.dumps([dict(ix) for ix in rows])
    return result


def insert_to_db(db, data):
    con = sqlite3.connect("Mylist.db")
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO {db} (tmdb_id,imdb_id)"
        f"VALUES( {data['id']},'{data['imdb_id']}');"
    )
    con.commit()
    con.close()
