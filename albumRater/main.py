import random as rand
import json
import os


#Functions
def loadAlbums():
    try:
        with open("albumRater/albums.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def addAlbum():
    print("Remember to check your spelling to ensure the system works as intended!")
    artistName = input("Enter Artist Name:")
    albumName = input("Enter Album name:")

    #Code to check whether artist exists:
    if artistName not in ratedAlbums:
        ratedAlbums[artistName] = {}
        print(f"New Artist {artistName} created!")
    
    #Code to check whether album from artist is already entered:
    if albumName in ratedAlbums[artistName]:
        print(f"{albumName} by {artistName} already exists!")
        return
    
    songs  = []
    songCounter = 0
    songAmount = int(input("How many songs does the album contain?"))
    
    while songCounter < songAmount:
        song = input("Song: ")
        songs.append(song)
        songCounter += 1

    ratedAlbums[artistName][albumName] = songs
    saveAlbums(ratedAlbums)
    print(json.dumps(ratedAlbums, indent=4))
    print(f"'{albumName}' by {artistName} saved!")




def saveAlbums(albums):
    with open("albumRater/albums.json", "w") as f:
        json.dump(albums, f, indent=4)

def printAlbums():
    ratedAlbums = loadAlbums()
    print(json.dumps(ratedAlbums, indent=4))

    for artist, albums in ratedAlbums.items():
        print(f"{artist}:")
        for album, songs in albums.items():
            print(f" {album}:")
            for song in songs:
                print(f"    - {song}")
    print()



# Main Code:
ratedAlbums = loadAlbums()

userChoice = int(input("""
---WELCOME TO ALBUM|RATER---

What features would you like to use?
  1: Add album
  2: View albums
  3: Edit an album
  4: Delete an album
"""))


print("\n-------SPACER-------\n")














