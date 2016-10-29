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
    cookie = random.randint(0, 2147483647)
    retransmit = False

    while(retransmit):
        try:
            req = protocol.package_request(991926251, cookie)

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(0.5)

            sock.sendto(req, (address, port))
            result = sock.recvfrom(16)
            retransmit = !protocol.good_response(result)
        except socket.timeout:
            retransmit = True;
