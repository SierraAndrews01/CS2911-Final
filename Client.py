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
            song = b'' + reciveUntilEnd(tcp_socket)
            song = song.decode()
            print(song)

            # Open file in binary write mode
            binary_file = open("my_file.flac", "wb")
            # Write bytes to file
            print(type(song))
            binary_file.writelines(song.encode())
            # Close file
            binary_file.close()
            # Play song
            wavFile = AudioSegment.from_file(binary_file, format = "flac")
            # Saves file to computer
            wavFile.export("tempFile.wav", format = "wav")
            play(wavFile)

        elif userRequest == 2:

            print('How many songs would you like to listen to: ')
            numSongs = input()
            fullans = b'2 \r\n numberOfSongs: ' + numSongs.encode() + b'\r\n '
            numSongs = int(numSongs)

            for i in range(numSongs):
                firstQuestion = 'What artist would you like to play: '
                print(firstQuestion)
                artistans = input()
                secondQuestion = 'What song title would you like to play: '
                print(secondQuestion)
                songans = input()
                fullans += b'artist: ' + artistans.encode() + b'\r\n' + b'song: ' + songans.encode() + b'\r\n'

            tcp_socket.sendall(fullans + b'\r\n')

        elif userRequest == 3:

            print('How many songs would you like: ')
            ans = input()
            tcp_socket.sendall(b'3 \r\n numberOfSongs: ' + ans.encode() + b'\r\n\r\n')

        elif userRequest == 4:

            print('What artist would you like to play: ')
            ans1 = input()
            print('What album would you like to play: ')
            ans2 = input()
            tcp_socket.sendall(b'4 \r\n artist: ' + ans1.encode() + b'\r\n album: ' + ans2.encode() + b'\r\n\r\n')

        elif userRequest == 5:

            print('What artist would you like to play: ')
            ans1 = input()
            print('What number of songs would you like to play by them (0 means grab all): ')
            ans2 = input()
            tcp_socket.sendall(b'5 \r\n artist: ' + ans1.encode() + b'\r\n numberOfSongs ' + ans2.encode() + b'\r\n\r\n')

        elif userRequest == 0:
            break
        # Use the info the server sends back to display the music to the user


def reciveUntilEnd(socket):
    count = 0
    message = b""
    while count != 4:
        currentByte = socket.recv(1)
        if currentByte == b'\r' or currentByte == b'\n':
            count += 1
        else:
            count = 0
            message += currentByte
    return message

if __name__ == "__main__":
    tcp_send(OTHER_HOST, TCP_Port)