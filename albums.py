#Defining a function that takes 2 pieces of info and assigns a 
#key to it
def build_album(artist_name, album_name, album_songs=None):
    """Builds a dictionary describing an album name"""
    album = {'artist': artist_name, 'album': album_name}
    if album_songs:
        album['songs'] = album_songs
    
    return album

album1 = build_album("Pink Floyd", "Dark Side", 12)
album2 = build_album("The Doors", "1967")
album3 = build_album("Guns n Roses", "Welcome to the Junlge")

print(album1['artist'])
print(album1['songs'])
print(album2)

artist = input("Please enter name of artist: ")
while artist != 'q':
    album = input("Enter name of album: ")
    ans = input("Do you know number of songs? (y/n)\n")
    if ans == "y":
        songs = input("Enter number of songs: ")
        alb = build_album(artist, album, songs)
    else:
        alb = build_album(artist, album)
    print(alb)
    
    artist = input("Please enter name of artist: ") 