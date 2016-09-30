#!/usr/bin/env python

import socket

server = "paris.cs.utexas.edu"
#server = "128.83.144.56"
port = 35603

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    (client, clientPort) = s.getsockname()
    dataout = "ex0 128.83.144.56-" + str(port) + " " + client + "-" + str(clientPort) + " 3933 R.Delfin.Garcia\n";
    #print("Sending ", dataout)
    s.send(dataout.encode('utf-8'))
    data = s.recv(512)
    s.close()
    print("Result: ", data)


