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

    # listen_address = ('', port)
    # server_socket.bind(listen_address)
    # server_socket.listen(num_connections)
    # Display any and all possible options the user could select
    # Create a file(messages) with the options
    header = 'Key (required),artist(optional),song(optional),number of songs(optional),album(optional),'
    + 'genres(optional)'
    optionOneDescription = 'Select a single song = 1 \r\n'
    optionTwoDescription = 'Select a certain number of specified songs = 2 \r\n'
    optionThreeDescription = 'Select a random number of songs = 3 \r\n'
    optionFourDescription = 'Select a specific album = 4 \r\n'
    optionFiveDescription = 'Select all songs of a specific artist = 5 \r\n'
    optionSixDescription = 'Select songs from a specific genre = 6 \r\n'
    totalDescription = optionOneDescription + optionTwoDescription + optionThreeDescription + optionFourDescription + optionFiveDescription + optionSixDescription
    askWhatOption = 'Which option would you like to select: \r\n\r\n'
    tcp_socket.sendall(totalDescription + askWhatOption)
    # Based on whatever number the user said, ask for the necessary requirements
    # Read input from command prompt
    userRequest = tcp_socket.recv()
    # TODO: Add a listener
    # TODO: Figure out how to properly receive data from user

    if userRequest == 1:
        print('What artist would you like to play: ')
        artistans = input()
        print('What song title would you like to play: ')
        songans = input()
        tcp_socket.sendall('1 \r\n artist: ' + artistans + '\r\n song: ' + songans)
    elif userRequest == 2:
        print('How many songs would you like to listen to: ')
        numSongs = input()
        fullans = '2 '
        for song in numSongs:
            firstQuestion = 'What artist would you like to play: '
            print(firstQuestion)
            artistans = input()
            secondQuestion = 'What song title would you like to play: '
            print(secondQuestion)
            songans = input()
            fullans += '\r\n' + 'artist: ' + artistans + '\r\n' + 'song: ' +songans + '\r\n'
        tcp_socket.sendall(fullans + '\r\n')
    elif userRequest == 3:
        print('How many songs would you like: ')

    elif userRequest == 4:
        firstQuestion = 'What artist would you like to play: \r\n'
        secondQuestion = 'What album would you like to play: \r\n'
        fullQuestion = firstQuestion + secondQuestion
        tcp_socket.send(fullQuestion)
    elif userRequest == 5:
        firstQuestion = 'What artist would you like to play: \r\n'
        secondQuestion = 'What number of songs would you like to play by them: \r\n'
        fullQuestion = firstQuestion + secondQuestion
        tcp_socket.send(fullQuestion)
    elif userRequest == 6:
        firstQuestion = 'What genre would you like to play: \r\n'
        secondQuestion = 'What number of songs would you like to play: \r\n'
        fullQuestion = firstQuestion + secondQuestion
        tcp_socket.send(fullQuestion)
    # Send info to server
    # Use the info the server sends back to display the music to the user

if __name__ == "__main__":
    tcp_send(OTHER_HOST, TCP_Port)