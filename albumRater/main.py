import random as rand
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "albums.json")

def loadAlbums():
    try:
        with open(JSON_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("albums.json is corrupted.")
        return {}

def saveAlbums(albums):
    with open(JSON_PATH, "w") as f:
        json.dump(albums, f, indent=4)

def addAlbum():
    print("Remember to check your spelling!")
    artistName = input("Enter Artist Name:")
    albumName = input("Enter Album name:")
    if artistName not in ratedAlbums:
        ratedAlbums[artistName] = {}
        print(f"New Artist {artistName} created!")
    if albumName in ratedAlbums[artistName]:
        print(f"{albumName} by {artistName} already exists!")
        return
    songs = []
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
    print(f"'{albumName}' by {artistName} saved!")

def printAlbums():
    ratedAlbums = loadAlbums()
    for artist, albums in ratedAlbums.items():
        print(f"{artist}:")
        for album, data in albums.items():
            print(f"  {album} — {data['rating']}/10:")
            for song in data['songs']:
                print(f"    - {song}")
    print()

def editAlbum():
    ratedAlbums = loadAlbums()
    artistName = input("Enter your artist:")
    if artistName not in ratedAlbums:
        print(f"Artist {artistName} not found.")
        return
    albumName = input("Enter album name:")
    if albumName not in ratedAlbums[artistName]:
        print(f"{albumName} by {artistName} not found.")
        return
    editChoice = int(input("""
  1: Rename the album
  2: Rename the artist
  3: Edit a song title
  4: Add a song
  5: Delete a song
"""))
    if editChoice == 1:
        newName = input("Enter new album name:")
        ratedAlbums[artistName][newName] = ratedAlbums[artistName].pop(albumName)
        print("Album renamed.")
    elif editChoice == 2:
        newName = input("Enter new artist name:")
        ratedAlbums[newName] = ratedAlbums.pop(artistName)
        print("Artist renamed.")
    elif editChoice == 3:
        songs = ratedAlbums[artistName][albumName]["songs"]
        for i, song in enumerate(songs):
            print(f"  {i+1}: {song}")
        songNum = int(input("Enter song number to edit:")) - 1
        newSong = input("Enter new song name:")
        songs[songNum] = newSong
        print(f"Song updated to {newSong}")
    elif editChoice == 4:
        newSong = input("Enter song to add:")
        ratedAlbums[artistName][albumName]["songs"].append(newSong)
        print(f"'{newSong}' added!")
    elif editChoice == 5:
        songs = ratedAlbums[artistName][albumName]["songs"]
        for i, song in enumerate(songs):
            print(f"  {i+1}: {song}")
        songNum = int(input("Enter song number to delete:")) - 1
        removed = songs.pop(songNum)
        print(f"'{removed}' deleted.")
    else:
        print(f"{editChoice} is invalid!")
        return
    saveAlbums(ratedAlbums)
    print("Changes saved!")

def deleteAlbum():
    print("\n--Make sure to spell your artist correctly--\n")
    artistName = input("Enter your artist:")
    if artistName not in ratedAlbums:
        print(f"Artist {artistName} not found.")
        return
    albumName = input("Enter album name:")
    if albumName not in ratedAlbums[artistName]:
        print(f"{albumName} by {artistName} not found.")
        return
    userConfirm = input(f"Are you sure you want to delete {albumName} by {artistName}? (y/n)")
    if userConfirm.lower() != "y":
        print("Cancelled.")
        return
    del ratedAlbums[artistName][albumName]
    if len(ratedAlbums[artistName]) == 0:
        del ratedAlbums[artistName]
        print(f"Artist {artistName} removed as they have no albums left.")
    saveAlbums(ratedAlbums)
    print("Album deleted!")

def topAlbums():
    ratedAlbums = loadAlbums()
    allAlbums = []
    for artist, albums in ratedAlbums.items():
        for album, data in albums.items():
            allAlbums.append((data['rating'], album, artist))
    allAlbums.sort(reverse=True)
    print("\n---TOP RATED ALBUMS---\n")
    for i, (rating, album, artist) in enumerate(allAlbums[:20]):
        print(f"  {i+1}. {album} by {artist} — {rating}/10")

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
  6: View top rated albums
"""))

if userChoice == 1:
    addAlbum()
elif userChoice == 2:
    printAlbums()
elif userChoice == 3:
    editAlbum()
elif userChoice == 4:
    deleteAlbum()
elif userChoice == 5:
    guessSong()
elif userChoice == 6:
    topAlbums()

print("\n-------SPACER-------\n")