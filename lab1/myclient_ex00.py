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
    port = 35605
    random.seed()
    cookie = 42
    retransmit = True
    count = 0

    while(retransmit and count < 5):
        count += 1
        try:
            req = protocol.package_request(111111111, cookie)

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(0.5)

            sock.sendto(req, (address, port))
            result = sock.recvfrom(16)
            resultString = result[0]
            retransmit = not(protocol.good_response(resultString, 111111111, cookie))
            protocol.print_raw(resultString)

        except socket.timeout:
            retransmit = True;
