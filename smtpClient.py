from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Computer networks are great!"
    endmsg = "\r\n.\r\n"


    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # Send HELLO command and print server response.

    helloCommand = 'HELO Mark\r\n'
    clientSocket.sendall(helloCommand.encode())
    # Fill in start

    mailfromCommand = 'MAIL FROM: <mail@mail.com>\r\n'
    clientSocket.sendall(mailfromCommand.encode())
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
   
    receiver = 'cubicmaara@gmail.com'
    toCommand = 'RCPT TO: <'+ receiver +'>\r\n'
    clientSocket.sendall(toCommand.encode())
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start

    dataCommand = 'DATA\r\n'
    print (dataCommand)
    clientSocket.sendall(dataCommand.encode())
    # Fill in end


    # Send message data.
    # Fill in start
    Subject = 'Bread'
    Text = "It's bad for you, don't eat it."

    message = "Subject: "+Subject+"\r\n\r\n"+Text
    clientSocket.sendall(message.encode())
    # Fill in end


    # Message ends with a single period, send message end and handle server response.

    # Fill in start
    endmsg = "\r\n.\r\n"
    clientSocket.sendall(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit_msg = "QUIT\r\n"
    clientSocket.sendall(quit_msg.encode())
    recv7 = clientSocket.recv(1024).decode()
    clientSocket.close()

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
