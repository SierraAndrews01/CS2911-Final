from socket import *
import os
import random

def MusicServer():
    server_socket = socket(AF_INET, SOCK_STREAM)
    listen_address = ('', 12345)
    server_socket.bind(listen_address)
    server_socket.listen()
    #message = b"4\r\n artist: ICE NINE KILLS\r\n album: The Predator Becomes The Prey\r\n\r\n"
    client, request_address = server_socket.accept()
    ONCE = True
    message = ""
    client.sendall(b"welcome to the music server")
    while True:
        message = reciveUntilEnd(client)
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

                                fileLocation = "C:/Users/kitzmann/Music/"+artist+"/"+sub+"/"+checkSong
                                file = open(fileLocation, "rb")
                                client.sendall(b"Length: " +str(os.stat(fileLocation).st_size).encode()+b'\r\n\r\n')
                                client.sendall(file.read(os.stat(fileLocation).st_size))
                                found = True
                                file.close()
                                break
                        if found:
                            break
            else:
                client.sendall(b"You are missing essential information\r\n\r\n")
        elif message[0:1] == "2":
            if "artist:" in message and "song:" in message and "numberOfSongs:" in message:
                artist = getInfo("artist:",message)
                song = getInfo("song:" , message)
                numberOfSongs = getInfo("numberOfSongs:", message)
                newMessage = message
                for i in range(int(numberOfSongs)):
                    found = False
                    print("C:/Users/kitzmann/Music/"+artist)
                    if os.path.exists("C:/Users/kitzmann/Music/"+artist):
                        subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                        for sub in subs:
                            if os.path.exists("C:/Users/kitzmann/Music/"+artist+"/"+sub):
                                songs = os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub)
                                for checkSong in songs:
                                    if checkSong[3:] == (song+".flac"):
                                        print("FOUND")
                                        fileLocation = "C:/Users/kitzmann/Music/"+artist+"/"+sub+"/"+checkSong
                                        file = open(fileLocation, "rb")
                                        client.sendall(b"Length: " +str(os.stat(fileLocation).st_size).encode()+b'\r\n\r\n')
                                        client.sendall(file.read(os.stat(fileLocation).st_size))
                                        found = True
                                        break
                                if found:
                                    break
                    newMessage = newMessage[newMessage.find("song:"):]
                    newMessage = newMessage[newMessage.find("\r\n"):]
                    artist = getInfo("artist:",newMessage)
                    song = getInfo("song:" , newMessage)
            else:
                client.sendall(b"You are missing essential information for this key\r\n\r\n")
        elif message[0:1] == "3":
            songs = []
            if "numberOfSongs:" in message:
                number = 0
                while number <  int(getInfo("numberOfSongs:", message)):
                    artist = random.choice(os.listdir("C:/Users/kitzmann/Music/"))
                    if os.path.isdir("C:/Users/kitzmann/Music/"+artist):
                        sub = random.choice(os.listdir("C:/Users/kitzmann/Music/"+artist))
                        song = random.choice(os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub))
                        if song not in songs:
                            if song[song.find("."):] == ".flac":
                                songs.append(song)
                                fileLocation = "C:/Users/kitzmann/Music/"+artist+"/"+sub+"/"+song
                                print(fileLocation)
                                file = open(fileLocation, "rb")
                                print(str(os.stat(fileLocation).st_size))
                                client.sendall(b"Length: " +str(os.stat(fileLocation).st_size).encode()+b'\r\n\r\n')
                                current = client.recv(1)
                                while  current != b'A':
                                    current = client.recv(1)
                                client.sendall(file.read(os.stat(fileLocation).st_size))
                                number += 1
                                current = client.recv(1)
                                while  current != b'A':
                                    current = client.recv(1)

            else:
                client.sendall(b"You are missing essential information for this key\r\n\r\n")
        elif message[0:1] == "4":
            if "artist:" in message and "album:" in message:
                artist = getInfo("artist:", message)
                album = getInfo("album:", message)
                songMessage = b''
                if os.path.exists("C:/Users/kitzmann/Music/"+artist):
                    subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                    if os.path.exists("C:/Users/kitzmann/Music/"+artist+"/"+album):
                        songs = os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+album)
                        for song in songs:
                            if song[song.find("."):] == ".flac":
                                fileLocation = "C:/Users/kitzmann/Music/"+artist+"/"+album+"/"+song
                                file = open(fileLocation, "rb")
                                client.sendall(b"Length: " +str(os.stat(fileLocation).st_size).encode()+b'\r\n\r\n')
                                client.sendall(file.read(os.stat(fileLocation).st_size))

            else:
                client.sendall(b"You are missing essential information for this key\r\n\r\n")
        elif message[0:1] == "5":
            songs = []
            songMessage = b''
            if "artist:" in message and "numberOfSongs:" in message:
                artist = getInfo("artist:",message)
                numberOfSongs = getInfo("numberOfSongs:", message)
                number = 0 
                print(numberOfSongs)
                while number < int(numberOfSongs):
                    subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                    sub = random.choice(subs)
                    print(sub)
                    song = random.choice(os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub))
                    print(song)
                    if song not in songs:
                        if song[song.find("."):] == ".flac":
                            songs.append(song)
                            fileLocation = "C:/Users/kitzmann/Music/"+artist+"/"+sub+"/"+song
                            file = open(fileLocation, "rb")
                            client.sendall(b"Length: " +str(os.stat(fileLocation).st_size).encode()+b'\r\n\r\n')
                            client.sendall(file.read(os.stat(fileLocation).st_size))
                            number += 1

            elif "artist:" in message:
                allSongs = []
                songMessage = b''
                artist = getInfo("artist:",message)
                if os.path.exists("C:/Users/kitzmann/Music/"+artist):
                    subs = os.listdir("C:/Users/kitzmann/Music/"+artist)
                    for sub in subs:
                        songs = os.listdir("C:/Users/kitzmann/Music/"+artist+"/"+sub)
                        for song in songs:
                           if song not in songs:
                            allSongs.append(song)
                            fileLocation = "C:/Users/kitzmann/Music/"+artist+"/"+sub+"/"+song
                            file = open(fileLocation, "rb")
                            client.sendall(b"Length: " +str(os.stat(fileLocation).st_size).encode()+b'\r\n\r\n')
                            client.sendall(file.read(os.stat(fileLocation).st_size))

            else:
                client.sendall(b"You are missing essential information for this key\r\n\r\n")

def reciveUntilEnd(socket):
    count = 0
    message = ""
    while count != 4:
        currentByte = socket.recv(1)
        if currentByte ==b'\r' or currentByte ==b'\n':
            count += 1
        else:
            count = 0
        message += currentByte.decode()
    return message

def getInfo(start, message):
    info = message[message.find(start):]
    info = info[info.find(":")+1:info.find("\r\n")].strip()
    return info


if __name__ == '__main__':
    MusicServer()