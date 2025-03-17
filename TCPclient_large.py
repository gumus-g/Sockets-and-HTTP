# Citation for the following function:
# Date: 1/20/2025
# Source URL: https://docs.python.org/3/howto/sockets.html
# Source URL: https://www.binarytides.com/python-socket-programming-tutorial/#google_vignette
# Source from: Kurose, J. F., & Ross, K. W. (2021). Computer networking : a top-down approach (Eighth edition.). Pearson.

import socket

# server 
serverName = 'gaia.cs.umass.edu'
serverPort = 80

# Create TCP client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect((serverName, serverPort))

sentence = input ("GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n")

# Send HTTP GET request
request = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n"
clientSocket.send(request.encode())

# receive the response
response = clientSocket.recv(4096)
while response:
        print(response.decode(), end='')  # Print data chunk by chunk
        response = clientSocket.recv(4096)       

print('Response from server:')
print(response.decode())

# Close the client socket
clientSocket.close()