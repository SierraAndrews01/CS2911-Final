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
    # Display any and all possible options the user could select
        # Create a file(messages) with the options
    header = 'Key (required),artist(optional),song(optional),number of songs(optional),album(optional),'
    + 'genres(optional)'
    optionOneDescription = 'Select a single song \r\n'
    optionTwoDescription = 'Select a certain number of specified songs \r\n'
    optionThreeDescription = 'Select a random number of songs \r\n'
    optionFourDescription = 'Select a specific album \r\n'
    optionFiveDescription = 'Select all songs of a specific artist \r\n'
    optionSixDescription = 'Select songs from a specific genre \r\n'
    totalDescription = optionOneDescription + optionTwoDescription + optionThreeDescription
    + optionFourDescription + optionFiveDescription + optionSixDescription
    askWhatOption = 'Which option would you like to select: '
    tcp_socket.sendall(totalDescription + askWhatOption)
    # Based on whatever number the user said, ask for the necessary requirements
    
    # Send info to server
    # Use the info the server sends back to display the music to the user

if __name__ == "__main__":
    tcp_send(OTHER_HOST, TCP_Port)