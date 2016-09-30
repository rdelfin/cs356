#!/usr/bin/env python

import socket

server = "paris.cs.utexas.edu"
serverIp = "128.83.144.56"
port = 35603
usernum = 3933          # I just really like this number
portResponse = 3933     # You have no idea how much
servernum = 4242        # Do I really need to explain this?
username = "R.DelfinGarcia"

# Returns a byte string with the request to be sent at connection start
def initialEx0Req(sip, sport, cip, cport, unum, uname):
    dataout = "ex0 "
    identifier = sip + "-" + str(sport) + " " + cip + "-" + str(cport)
    dataout += identifier + " "
    dataout += str(unum) + " "
    dataout += uname + "\n"

    return dataout.encode('utf-8')



def secondEx0Req(unumInc, serverNum):
    dataout = "ex0 "
    dataout += str(unumInc) + " "
    dataout += str(serverNum + 1) + "\n"

    return dataout.encode('utf-8')



def initialEx1Req(sip, sport, cip, cport, unum, uname):
    dataout = "ex1 "
    identifier = sip + "-" + str(sport) + " " + cip + "-" + str(cport)
    dataout += identifier + " "
    dataout += str(unum) + " "
    dataout += uname + "\n"

    return dataout.encode('utf-8')


def ex0(client, clientPort, clientS):
    req1 = initialEx0Req(serverIp, port, client, clientPort, usernum, username)
    print("Request 1: ", req1)
    clientS.send(req1)

    line1 = clientS.recv(512)    # For reasons unknown, python only receives one line at a time. This receives the first line (server info + timestamp)
    line2 = clientS.recv(512)    # This receives the status code, as well as the result (OK num+1 Name randomNumber)

    print("Response: \n\t", line1, "\n\t",  line2, "\n")

    responseList = line2.decode().split(" ")

    unumInc = responseList[1]
    serverNum =int(responseList[3].strip())

    req2 = secondEx0Req(unumInc, serverNum)
    print("Request 2: ", req2)
    clientS.send(req2)

    line1b = clientS.recv(512)

    print("Result: ", line1b)

def ex1ServerCall(servernum):
    return ("CS 356 server calling " + int(servernum) + "\n").encode('utf-8')

def ex1(client, clientPort, clientS, serverS):
    req1 = initialEx1Req(serverIp, port, client, portResponse, usernum, username)
    print("Request 1: ", req1)
    clientS.send(req1)

    line1 = clientS.recv(512)
    line2 = clientS.recv(512)

    print("Response: \n\t", line1, "\n\t",  line2, "\n")



    (responsesocket, addr) = serverS.accept()

    sock2msg = ex1ServerCall(servernum)
    responsesocket.send(sock2msg)

    print("Sent over socket 2: ", sock2msg, "\n")

    responsesocket.close()
    serverS.close()

    line1b = clientS.recv(512)
    line2b = clientS.recv(512)


    print("Response: \n\t", line1, "\n\t",  line2, "\n")


if __name__ == '__main__':
    clientS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientS.connect((server, port))
    (client, clientPort) = clientS.getsockname()

    serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverS.bind((socket.gethostname(), portResponse))
    serverS.listen(5)

    ex1(client, clientPort, clientS, serverS)

    clientS.close()


