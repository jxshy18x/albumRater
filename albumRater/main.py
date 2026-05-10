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

    albumRating = int(input("Rate this album (1-10):"))
    while albumRating < 1 or albumRating > 10:
        print("Please enter a number between 1 and 10")
        albumRating = int(input("Rate this album (1-10):"))

    ratedAlbums[artistName][albumName] = {
        "songs": songs,
        "rating": albumRating
    }
    saveAlbums(ratedAlbums)
    print(json.dumps(ratedAlbums, indent=4))
    print(f"'{albumName}' by {artistName} saved!")

def saveAlbums(albums):
    with open("albumRater/albums.json", "w") as f:
        json.dump(albums, f, indent=4)

def printAlbums():
    ratedAlbums = loadAlbums()
    for artist, albums in ratedAlbums.items():
        print(f"{artist}:")
        for album, data in albums.items():
            print(f"  {album} — {data['rating']}/10:")
            for song in data['songs']:
                print(f"    - {song}")
    print()

#Edit the information within an album
def editAlbum():
    ratedAlbums = loadAlbums()

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
    
    editChoice = int(input("""
        1: Rename the album
        2: Rename the artist
        3: Edit a song title
        4: Add a song
        5: Delete a song
    """))
        
    if editChoice == 1:
        renameAlbum = input("Enter album name:")
        ratedAlbums[artistName][renameAlbum] = ratedAlbums[artistName].pop(albumName)
        print("Album name changed.")
    
    elif editChoice == 2:
        renameArtist = input("Enter artist name:")
        ratedAlbums[renameArtist] = ratedAlbums.pop(artistName)
    
    elif editChoice == 3:
        songs = ratedAlbums[artistName][albumName]
        for i, song in enumerate(songs):
            print(f" {i + 1}: {song}")
        songNum = int(input("Enter song number to edit:")) - 1
        newSong = input("Enter new song name:")
        songs[songNum] = newSong
        print(f"Song updated to {newSong}")

    elif editChoice == 4:
        print("")
    
    elif editChoice == 5:
        print("")
    
    else:
        print(f"{editChoice} is invalid!")
        return
    saveAlbums(ratedAlbums)
    print("Changes saved!")

#Deletes album at the user's request
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

#Song guessing game, guess what album the song is off of!
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
  6: View top 20 rated albums
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














