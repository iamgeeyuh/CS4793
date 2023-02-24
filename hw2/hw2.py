from socket import *
import base64
# Choose a mail server (e.g. NYU. mail server) and call it mailserver
# Code Start dig nyu.edu MX +short # Code End
mailserver = 'smtp.nyu.edu'
serverPort = 25
# Create socket and establish TCP connection with mailserver
# Code Start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))
# Code End
tcp_resp = clientSocket.recv(1024).decode()
print(tcp_resp)
# Send HELO command to begin SMTP handshake.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
helo_resp = clientSocket.recv(1024).decode()
print(helo_resp)
# Send MAIL FROM command and print response.
# Code Start
mailFrom = "Mail from: <jia.huang@nyu.edu>\r\n"
clientSocket.send(mailFrom.encode())
from_resp = clientSocket.recv(1024).decode()
print(from_resp)
# Code End
# Send RCPT TO command and print server response.
# Code Start
rcptTo = "RCPT TO: <jia.huang@nyu.edu>\r\n"
clientSocket.send(rcptTo.encode())
to_resp = clientSocket.recv(1024).decode()
print(to_resp)
# Code End
# Send DATA command and print server response.
# Code Start
data = 'DATA\r\n'
clientSocket.send(data.encode())
data_resp = clientSocket.recv(1024).decode()
print(data_resp)
# Code End
# Send email data.
# Code Start
clientSocket.send('Subject: Testing!!!!!!! \r\n'.encode())
# Code End
# Send msg to close email msg.
# Code Start
msg = 'Hello World :D\r\n'
msg += '\r\n'
msg += 'Best,\r\n'
msg += 'Jia\r\n'
msg += '.\r\n'
clientSocket.send(msg.encode())
sent_resp = clientSocket.recv(1024).decode()
print(sent_resp)
# Code End
# Send QUIT command and get server response.
# Code Start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
quit_resp = clientSocket.recv(1024).decode()
print(quit_resp)
# Code End
clientSocket.close()
