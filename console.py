from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

album_repo.delete_all()
artist_repo.delete_all()

artist1 = Artist("AC/DC")
artist2 = Artist("Black Sabbath")
artist3 = Artist("Blue Öyster Cult")

album1 = Album("Black Sabbath","Heavy Metal",artist2)
album2 = Album("Crazy Train","Heavy Metal",artist2)
album3 = Album("Fire Of Unknown Origin", "Alt Rock",artist3)

artist_repo.save(artist1)
artist_repo.save(artist2)
artist_repo.save(artist3)
album_repo.save(album1)
album_repo.save(album2)
album_repo.save(album3)


