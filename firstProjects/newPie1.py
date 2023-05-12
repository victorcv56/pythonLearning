def fave_albums():
    """Create dictionary with favorite albums by artists"""
    albums = {}
    active = True #flag to terminate program
    
    print("Type 'quit' to terminate")
    
    album_name = input("\nAlbum Name: ")
    while active: #loop that will fill dictionary

        artist_name = input("Artist: ")
        albums[album_name] = artist_name 

        album_name = input("\nAlbum Name: ")
        if album_name == 'quit':
            active = False

    
    return albums #returns filled dictionary
        
albums = fave_albums()

for album_name, artist_name in albums.items(): #loop to print dictionary
    print(f"{album_name} was performed by {artist_name.title()}")

