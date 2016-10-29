import struct
from util import *

# struct {
#   short header; = 0 0 00000101100100
#   byte labN;   = 00000001
#   byte version; = 00000111
#   int clientCookie;
#   int requestData;
#   short checksum;
#   short result;
# }


def package_request(requestData, clientCookie):
    header = 356
    labN = 1
    version  = 7
    checksum = 0
    result = 0

    tempPackage  = struct.pack('!HBBIIHH', header, labN, version, clientCookie, requestData, checksum, result)
    checksum = calc_checksum(tempPackage)
    return struct.pack('!HBBIIHH', header, labN, version, clientCookie, requestData, checksum, result)

def print_raw(response):
    for i in range(4):
        shortLow = get_short_network(response, i*4)
        shortHight = get_short_network(response, i*4 + 2)
        lowString = "{0:b}".format(shortLow)
        highString = "{0:b}".format(shortHight)
        print(lowString, " ", highString)

def calc_checksum(tempPackage):
    checksumTotal = 0
    for i in range(8):
        shortVal = get_short_network(tempPackage, i*2)
        checksumTotal = ones_comp_add16(checksumTotal, shortVal)
    return checksumTotal
