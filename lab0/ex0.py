#!/usr/bin/env python3

import socket

server = "paris.cs.utexas.edu"
serverIp = "128.83.144.56"
port = 35603
usernum = 3933
actiontype = "ex0"
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

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    (client, clientPort) = s.getsockname()

    req1 = initialEx0Req(serverIp, port, client, clientPort, usernum, username)
    print("Request 1: ", req1)
    s.send(req1)

    line1 = s.recv(512)    # For reasons unknown, python only receives one line at a time. This receives the first line (server info + timestamp)
    line2 = s.recv(512)    # This receives the status code, as well as the result (OK num+1 Name randomNumber)

    print("Result: ", line1, "\n", line2)

    responseList = line2.decode().split(" ")

    unumInc = responseList[1]
    serverNum =int(responseList[3].strip())

    req2 = secondEx0Req(unumInc, serverNum)
    print("Request 2: ", req2)
    s.send(req2)

    line1b = s.recv(512)

    print("Result: ", line1b)

    s.close()


