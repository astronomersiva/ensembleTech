import socket
import threading

host = "192.168.0.32"
port = 18200

serverConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverConn.connect((hote, port))

def First_whait_user():
    message = b""
    while message != b"exit":
        messageReceived = serverConn.recv(1024)
        print(messageReceived.decode())
        messageToSend = raw_input("> ")
        
        # Peut planter si vous tapez des caracteres speciaux
        messageToSend = messageToSend.encode()
        # On envoie le message
        serverConn.send(messageToSend)

        
first  = threading.Thread(target=First_whait_user)
first.start()

