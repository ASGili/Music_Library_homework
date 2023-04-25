from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    row = run_sql(sql,values)
    id = row[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    row = run_sql(sql)
    
def select(artist_id):
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [artist_id]
    row = run_sql(sql, values)[0]
    if row:
        artist = Artist(row['name'],row['id'])
    return artist
