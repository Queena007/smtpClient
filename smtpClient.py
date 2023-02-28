from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Computer networks are great!"
    endmsg = "\r\n.\r\n"


    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    # mailserver = ''
    # port = 1025

    # mailserver = 'smtp.gmail.com'
    # port = 587

    clientSocket = socket(AF_INET,SOCK_STREAM)

    #clientSocket.bind((mailserver, port))
    clientSocket.connect((mailserver, port))

    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # print('test')

    # print(recv) #You can use these print statement to validate return codes from the server.

    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELLO command and print server response.

    helloCommand = 'HELO Mark\r\n'

    clientSocket.sendall(helloCommand.encode())
   
    recv1 = clientSocket.recv(1024).decode()

    # print(recv1)

    # if recv1[:3] != '250':

    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
   
    # Fill in start

    mailfromCommand = 'MAIL FROM: <mail@mail.com>\r\n'
    clientSocket.sendall(mailfromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #     print('mail from 250 reply not received from server.')

    # Fill in end


    # Send RCPT TO command and handle server response.
    # Fill in start
   
    # receiver = input("Send email to: ")
    receiver = 'cubicmaara@gmail.com'

    toCommand = 'RCPT TO: <'+ receiver +'>\r\n'

    # print (toCommand)

    clientSocket.sendall(toCommand.encode())

    recv3 = clientSocket.recv(1024).decode()

    # print (recv3)

    # if recv3[:3] != '250':
    #     print('250 reply not received from server.')

    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start

    dataCommand = 'DATA\r\n'
    print (dataCommand)
    clientSocket.sendall(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print (recv4)
    # if recv4[:3] != '250':
    #     print('data 250 reply not received from server.')

    # Fill in end


    # Send message data.
    # Fill in start
    # Subject = input("Subject: ")
    # Text = input("Message: ")
    Subject = 'Bread'
    Text = "It's bad for you, don't eat it."

    message = "Subject: "+Subject+"\r\n\r\n"+Text
    clientSocket.sendall(message.encode())
    recv5 = clientSocket.recv(1024).decode()
    # print (recv5)
    # if recv5[:3] != '250':
    #     print('message 250 reply not received from server.')

    # Fill in end


    # Message ends with a single period, send message end and handle server response.

    # Fill in start
    endmsg = "\r\n.\r\n"
    clientSocket.sendall(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6)
    # if recv6[:3] != '250':
    #     print('end msg 250 reply not received from server.')


    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit_msg = "QUIT\r\n"
    clientSocket.sendall(quit_msg.encode())
    recv7 = clientSocket.recv(1024).decode()
    # print (recv7)
    # if recv7[:3] != '250':
    #     print('quit 250 reply not received from server.')

    clientSocket.close()

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
