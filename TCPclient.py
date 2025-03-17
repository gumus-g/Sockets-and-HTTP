# Citation for the following function:
# Date: 1/20/2025
# Source URL: https://docs.python.org/3/howto/sockets.html
# Source URL: https://www.binarytides.com/python-socket-programming-tutorial/#google_vignette
# Source from: Kurose, J. F., & Ross, K. W. (2021). Computer networking : a top-down approach (Eighth edition.). Pearson.

import socket


# server
serverName = 'gaia.cs.umass.edu'
serverPort = 80

# create TCP client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the server
clientSocket.connect((serverName,serverPort))

# Set the input sentence
sentence = input ("GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n")

# Send HTTP GET request
request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n"
clientSocket.send(request.encode())

# Receive the response
response = clientSocket.recv(4096) #adjust buffor for large responses

print('Response from server:')
print(response.decode())

# Close the client socket
clientSocket.close()