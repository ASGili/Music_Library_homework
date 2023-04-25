from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repo as artist_repo

def save(album):
    sql = "INSERT INTO albums (title,genre,artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    row = run_sql(sql, values)
    id = row[0]['id']   
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    row = run_sql(sql)

def select(album_id):
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [album_id]
    row = run_sql(sql,values)[0]
    if row:
        artist = artist_repo.select(row['artist_id'])
        album = Album(row['title'],row['genre'],artist)
    return album