from socket import *

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
        optionFiveDescription = 'Select all songs of a specific artist = 5 \r\n'
        optionSixDescription = 'Select songs from a specific genre = 6 \r\n'
        totalDescription = optionOneDescription + optionTwoDescription + optionThreeDescription + optionFourDescription + optionFiveDescription + optionSixDescription
        askWhatOption = 'Which option would you like to select: \r\n\r\n'
        print(totalDescription + askWhatOption)
        userRequest = int(input())
        # TODO: Add a listener
        if userRequest == 1:
            print('What artist would you like to play: ')
            artistans = input()
            print('What song title would you like to play: ')
            songans = input()
            tcp_socket.sendall(b'1 \r\n artist: ' + artistans.encode() + b'\r\n song: ' + songans.encode() + b'\r\n\r\n')
        elif userRequest == 2:
            print('How many songs would you like to listen to: ')
            numSongs = input()
            fullans = b'2 \r\n numberOfSongs: ' + numSongs.encode()
            numSongs = int(numSongs)
            for i in range(numSongs):
                firstQuestion = 'What artist would you like to play: '
                print(firstQuestion)
                artistans = input()
                secondQuestion = 'What song title would you like to play: '
                print(secondQuestion)
                songans = input()
                fullans += b'\r\n artist: ' + artistans.encode() + b'\r\n' + b'song: ' + songans.encode() + b'\r\n'
            tcp_socket.sendall(fullans + b'\r\n')
        elif userRequest == 3:
            print('How many songs would you like: ')
            ans = int(input())
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
            print('What number of songs would you like to play by them: ')
            ans2 = int(input())
            tcp_socket.sendall(b'5 \r\n artist: ' + ans1.encode() + b'\r\n numberOfSongs ' + ans2.encode() + b'\r\n\r\n')
        elif userRequest == 6:
            print('What genre would you like to play: ')
            ans1 = input()
            print('What number of songs would you like to play: ')
            ans2 = int(input())
            tcp_socket.sendall(b'6 \r\n genre: ' + ans1.encode() + b'\r\n numberOfSongs: ' + ans2.encode() + b'\r\n\r\n')
        # Use the info the server sends back to display the music to the user

if __name__ == "__main__":
    tcp_send(OTHER_HOST, TCP_Port)