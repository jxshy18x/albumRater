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

def editAlbum():
    ratedAlbums = loadAlbums()

def deleteAlbum():
    print("\n--Make sure to spell your artist correctly--\n")
    
    #Checking artist name exists
    artistName = input("Enter your artist:")
    if artistName not in ratedAlbums:
        print(f"Artist {artistName}, not found in file.")
        return
    
    #Checking album exists
    albumName = input("Enter album name:")
    if albumName not in ratedAlbums[artistName]:
        print(f"{albumName} by {artistName} not found in file.")
        return
    
    #Ask user to confirm before deletion
    userConfirm = input(f"Are you sure you would like to delete {albumName} by {artistName}? (y/n)")
    if userConfirm.lower() != "y":
        print("Deleting process stopped")
        return
    
    del ratedAlbums[artistName][albumName]

    #if artist has no albums left, remove the artist
    if len(ratedAlbums[artistName]) == 0:
        del ratedAlbums[artistName]
        print(f"Artist: {artistName}, removed due to no logged albums.")

    saveAlbums(ratedAlbums)
    


def guessSong():
    print("")


# Main Code:
ratedAlbums = loadAlbums()

userChoice = int(input("""
---WELCOME TO ALBUM|RATER---

What features would you like to use?
  1: Add album
  2: View albums
  3: Edit an album
  4: Delete an album
  5: Play the guessing game
"""))

if userChoice == 1:
    addAlbum()
elif userChoice == 2:
    printAlbums()
elif userChoice == 3:
    editAlbum()
elif userChoice == 4:
    deleteAlbum()

print("\n-------SPACER-------\n")














