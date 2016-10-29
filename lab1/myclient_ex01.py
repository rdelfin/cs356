#! /usr/bin/env python

import random
import socket
import protocol

# M F     356         Lab #     Version
# 0 0 00000101100100 00000001  00000111

#          Client cookie
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#          Request Data (SSN)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#    Checksum      O     Result
# %%%%%%%%%%%%%%%% % %%%%%%%%%%%%%%%


if __name__ == "__main__":

    address = "paris.cs.utexas.edu"
    port = 35607
    random.seed()
    cookie = 42
    retransmit = True
    count = 0

    while(retransmit and count < 5):
        count += 1
        try:
            ssn = input('Enter a social security number: ')     # Ask for input
            req = protocol.package_request(ssn, cookie)         # Create request according to protocol

            # Create socket and set timeout
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(0.5)

            # Send and recieve data
            sock.sendto(req, (address, port))
            result = sock.recvfrom(16)

            # Get string (tupple is returned by socket)
            resultString = result[0]

            # Determine if it's necessary to restransmit
            retransmit = not(protocol.good_response(resultString, ssn, cookie))
            if(not(retransmit)):
                print("P.O. Box: ", protocol.get_result(resultString))

        # Catch timeout
        except socket.timeout:
            retransmit = True;
