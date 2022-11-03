from socket import *
import os
import random

def MusicServer():
    server_socket = socket(AF_INET, SOCK_STREAM)
    listen_address = ('', 12345)
    server_socket.bind(listen_address)
    server_socket.listen()
    message = b"4\r\n artist: ICE NINE KILLS\r\n album: The Predator Becomes The Prey\r\n\r\n"
    ONCE = True
    while ONCE:
        #client, request_address = server_socket.accept()
        #client.sendall(b"Hello and welcome to the Music Server\r\n\r\n")
        #message = reciveUntilEnd(client)
        if 
        message = message.decode()
        if message[0:1] == "1":
            found = False
            if "artist:" in message and "song:" in message:
                artist = getInfo("artist:",message)
                song = getInfo("song:" , message)
                if os.path.exists("C:/Users/kitzmann/Music/"+artist):
                    subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                    for sub in subs:
                        songs = os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub)
                        for checkSong in songs:
                            if checkSong[3:] == (song+".flac"):
                                print("FOUND")
                                found = True
                                break
                        if found:
                            break
            else:
                print("BAD")
                #client.sendall(b"You are missing essential information\r\n\r\n")
        elif message[0:1] == "2":
            if "artist:" in message and "song:" in message and "numberOfSongs:" in message:
                artist = getInfo("artist:",message)
                song = getInfo("song:" , message)
                numberOfSongs = getInfo("numberOfSongs:", message)
                newMessage = message
                for i in range(int(numberOfSongs)):
                    print(artist)
                    print(song)
                    found = False
                    if os.path.exists("C:/Users/kitzmann/Music/"+artist):
                        subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                        for sub in subs:
                            songs = os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub)
                            for checkSong in songs:
                                if checkSong[3:] == (song+".flac"):
                                    print("FOUND")
                                    found = True
                                    break
                            if found:
                                break
                    newMessage = newMessage[newMessage.find("song:"):]
                    newMessage = newMessage[newMessage.find("\r\n"):]
                    artist = getInfo("artist:",newMessage)
                    song = getInfo("song:" , newMessage)
            else:
                pass
                #client.sendall(b"You are missing essential information for this key\r\n\r\n")
        elif message[0:1] == "3":
            songs = []
            if "numberOfSongs:" in message:
                number = 0
                while number <  int(getInfo("numberOfSongs:", message)):
                    artist = random.choice(os.listdir("C:/Users/kitzmann/Music/"))
                    if os.path.isdir("C:/Users/kitzmann/Music/"+artist):
                        sub = random.choice(os.listdir("C:/Users/kitzmann/Music/"+artist))
                        song = random.choice(os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub))
                        if song not in songs and song.endswith(".flac"):
                            songs.append(song)
                            number += 1
                        print(artist)
                        print(sub)
                print(songs)

            else:
                pass
                #client.sendall(b"You are missing essential information for this key\r\n\r\n")
        elif message[0:1] == "4":
            if "artist:" in message and "album:" in message:
                artist = getInfo("artist:", message)
                album = getInfo("album:", message)
                if os.path.exists("C:/Users/kitzmann/Music/"+artist):
                    subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                    if os.path.exists("C:/Users/kitzmann/Music/"+artist+"/"+album):
                        songs = os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+album)
                print(songs)

            else:
                pass
                #client.sendall(b"You are missing essential information for this key\r\n\r\n")
        elif message[0:1] == "5":
            songs = []
            if "artist:" in message and "numberOfSongs:" in message:
                artist = getInfo("artist:",message)
                numberOfSongs = getInfo("numberOfSongs:", message)
                number = 0 
                while number < int(numberOfSongs):
                    subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                    sub = random.choice(subs)
                    song = random.choice(os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub))
                    if song not in songs:
                        songs.append(song)
                        number += 1
                print(songs)

            elif "artist:" in message:
                allSongs = []
                artist = getInfo("artist:",message)
                if os.path.exists("C:/Users/kitzmann/Music/"+artist):
                    subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                    for sub in subs:
                        songs = os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub)
                        for song in songs:
                           if song not in songs:
                            allSongs.append(song)  
                    print(allSongs)
            else:
                pass
                #client.sendall(b"You are missing essential information for this key\r\n\r\n")
        elif message[0:1] == "6":
            if "numberOfSongs:" in message and "genre:" in message:
                pass
            else:
                pass
                #client.sendall(b"You are missing essential information for this key\r\n\r\n")
        else:
            #client.sendall(b"Key value is not recognized\r\n\r\n")
            print("BIGBAD")
        ONCE = False

def reciveUntilEnd(socket):
    count = 0
    message = ""
    while count != 4:
        currentByte = socket.recv(1)
        if currentByte ==b'\r' or currentByte ==b'\n':
            count += 1
        else:
            count = 0
        message += currentByte
    return

def getInfo(start, message):
    info = message[message.find(start):]
    info = info[info.find(":")+1:info.find("\r\n")].strip()
    return info


if __name__ == '__main__':
    MusicServer()