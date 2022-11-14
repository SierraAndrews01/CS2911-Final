import io
from socket import *
from pydub import AudioSegment
from pydub.playback import play

# TCP Port
TCP_Port = 12345

# Address of the 'other' ('server') host that should be connected to for 'send' operations.
# When connecting on one system, use 'localhost'
# When 'sending' to another system, use its IP address (or DNS name if it has one)
# OTHER_HOST = '155.92.x.x'
OTHER_HOST = "localhost"

def tcp_send(server_host, server_port):
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect((server_host, server_port))
    # TODO: Fix listener lines
    # TODO: add a 0 option to exit
    # TODO: Receive welcome message
    # TODO: save/listen to files

    welcomeMessage = tcp_socket.recv(27)
    print(welcomeMessage.decode())

    while True:
        # listen_address = ('', port)
        # server_socket.bind(listen_address)
        # server_socket.listen(num_connections)
        # Display any and all possible options the user could select
        # Create a file(messages) with the options

        header = 'Key (required),artist(optional),song(optional),number of songs(optional),album(optional),' + 'genres(optional)'

        optionOneDescription = 'Select a single song = 1 \r\n'
        optionTwoDescription = 'Select a certain number of specified songs = 2 \r\n'
        optionThreeDescription = 'Select a random number of songs = 3 \r\n'
        optionFourDescription = 'Select a specific album = 4 \r\n'
        optionFiveDescription = 'Select a specific number of songs from a specific artist = 5 \r\n'
        optionSixDescription = 'To exit the program = 0 \r\n'

        totalDescription = optionOneDescription + optionTwoDescription + optionThreeDescription + optionFourDescription + optionFiveDescription + optionSixDescription
        askWhatOption = 'Which option would you like to select: \r\n\r\n'
        print(totalDescription + askWhatOption)
        userRequest = int(input())

        if userRequest == 1:

            print('What artist would you like to play: ')
            artistans = input()
            print('What song title would you like to play: ')
            songans = input()
            tcp_socket.sendall(b'1 \r\n artist: ' + artistans.encode() + b'\r\n song: ' + songans.encode() + b'\r\n\r\n')

            length = reciveUntilEnd(tcp_socket)
            actualLength = length[7:]
            song = b'' + tcp_socket.recv(int(actualLength))

            # Open file in binary write mode
            binary_file = open(artistans+" "+ songans+ " " +".flac", "wb")
            # Write bytes to file
            listSong = []
            listSong.append(song)
            binary_file.writelines(listSong)
            # Close file
            binary_file.close()

        elif userRequest == 2:
            artistNames = []
            songNames = []

            print('How many songs would you like to listen to: ')
            numSongs = input()
            fullans = b'2 \r\n numberOfSongs: ' + numSongs.encode() + b'\r\n '
            numSongs = int(numSongs)

            for i in range(numSongs):
                firstQuestion = 'What artist would you like to play: '
                print(firstQuestion)
                artistans = input()
                artistNames.append(artistans)
                secondQuestion = 'What song title would you like to play: '
                print(secondQuestion)
                songans = input()
                songNames.append(songans)
                fullans += b'artist: ' + artistans.encode() + b'\r\n' + b'song: ' + songans.encode() + b'\r\n'
            tcp_socket.sendall(fullans + b'\r\n')

            for i in range(numSongs):
                length = reciveUntilEnd(tcp_socket)
                tcp_socket.sendall(b'A')
                actualLength = length[7:]
                song = b'' + tcp_socket.recv(int(actualLength))
                binary_file = open(artistNames[i]+ " " + songNames[i] + " " + str(i) + ".flac", "wb")
                listSong = []
                listSong.append(song)
                binary_file.writelines(listSong)
                binary_file.close()

        elif userRequest == 3:

            print('How many songs would you like: ')
            ans = input()
            tcp_socket.sendall(b'3 \r\n numberOfSongs: ' + ans.encode() + b'\r\n\r\n')

            for i in range(int(ans)):
                length = reciveUntilEnd(tcp_socket)
                tcp_socket.sendall(b'A')
                actualLength = length[8:]
                song = b'' + tcp_socket.recv(int(actualLength))
                binary_file = open("song" + str(i) + ".flac", "wb")
                listSong = []
                listSong.append(song)
                binary_file.writelines(listSong)
                binary_file.close()
                tcp_socket.sendall(b'A')
               

        elif userRequest == 4:

            print('What artist would you like to play: ')
            ans1 = input()
            print('What album would you like to play: ')
            ans2 = input()
            tcp_socket.sendall(b'4 \r\n artist: ' + ans1.encode() + b'\r\n album: ' + ans2.encode() + b'\r\n\r\n')
            numSongs = reciveUntilEnd(tcp_socket)
            for i in range(int(numSongs[8:])):
                length = reciveUntilEnd(tcp_socket)
                tcp_socket.sendall(b'A')
                actualLength = length[8:]
                song = b'' + tcp_socket.recv(int(actualLength))

                # Open file in binary write mode
                binary_file = open(ans1+" "+ ans2 +" "+str(i)+".flac", "wb")
                # Write bytes to file
                listSong = []
                listSong.append(song)
                binary_file.writelines(listSong)
                # Close file
                binary_file.close()

        elif userRequest == 5:

            print('What artist would you like to play: ')
            ans1 = input()
            print('What number of songs would you like to play by them (0 means grab all): ')
            ans2 = input()
            tcp_socket.sendall(b'5 \r\n artist: ' + ans1.encode() + b'\r\n numberOfSongs: ' + ans2.encode() + b'\r\n\r\n')


            if ans2 == "0":
                numSongs2 = reciveUntilEnd(tcp_socket)[8:]
                tcp_socket.sendall(b'A')
                
            else:
                numSongs2 = int(ans2)

            for i in range(int(numSongs2)):
                length = reciveUntilEnd(tcp_socket)
                tcp_socket.sendall(b'A')
                actualLength = length[7:]
                song = b'' + tcp_socket.recv(int(actualLength))
                binary_file = open(ans1 + " " +str(i) + ".flac", "wb")
                listSong = []
                listSong.append(song)
                binary_file.writelines(listSong)
                binary_file.close()

        elif userRequest == 0:
            tcp_socket.sendall(b'0 \r\n\r\n')
            tcp_socket.close()
            break

def reciveUntilEnd(socket):
    count = 0
    message = ""
    while count != 4:
        currentByte = socket.recv(1)
        if currentByte == b'\r' or currentByte == b'\n':
            count += 1
        else:
            count = 0
            message += currentByte.decode()
    return message

if __name__ == "__main__":
    tcp_send(OTHER_HOST, TCP_Port)