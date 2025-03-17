# Citation for the following function:
# Date: 1/20/2025
# Source URL: https://docs.python.org/3/howto/sockets.html
# Source URL: https://www.binarytides.com/python-socket-programming-tutorial/#google_vignette
# Source from: Kurose, J. F., & Ross, K. W. (2021). Computer networking : a top-down approach (Eighth edition.). Pearson.


import socket	#for sockets

#server
serverIP = '127.0.0.1'
serverPort = 45000 # You can pick any available port > 1023

#create an AF_INET, STREAM socket (TCP)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)


print(f"Socket created and server is listening on http://127.0.0.1:{serverPort}\r\n")

while True:
    #accept connection from client
    connectionSocket, addr = serverSocket.accept()   

    #receive and print request from client 
    request = connectionSocket.recv(1024).decode()
    print("Request from client: ")
    print(request)
    

    # Send HTTP response   
    data =  "HTTP/1.1 200 OK\r\n"\
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
            "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
    connectionSocket.send(data.encode())
    
    # Close connection socket
    connectionSocket.close()
