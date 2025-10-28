def make_album(artist, title):
    album = {"artist": artist, "title": title}
    return album

while True:
    print("\nEnter album information (type 'quit' to stop):")
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break
    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    album_info = make_album(artist, title)
    print(album_info)