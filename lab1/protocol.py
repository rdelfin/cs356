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
    print("Pre-checksum package:")
    print_raw(tempPackage)
    checksum = get_checksum(tempPackage)
    result = struct.pack('!HBBIIHH', header, labN, version, clientCookie, requestData, checksum, result)
    print("Post-checksum package (", checksum, "):")
    print_raw(result)
    print("")
    return result

def good_response(response, ssn, cookie):
    data = struct.unpack('!HBBIIHH', response)
    header = data[0]
    labN = data[1]
    version = data[2]
    cookieRsp = data[3]
    requestData = data[4]
    checksum = data[5]
    result = data[6]

    if(labN != 1):
        return False

    if(((header & 0x4000) >> 14) != 1):
        print("Not response")
        return False
    if(ssn != requestData):
        print("different SSN")
        return False
    if(cookie != cookieRsp):
        print("different cookie")
        return False
    if(((result & 0x8000) >> 15) == 1):
        print("Error was returned by server: ", (result & 0x7fff))
        return False

    tempPackage  = struct.pack('!HBBIIHH', header, labN, version, cookieRsp, requestData, 0, result)

    computedChecksum = get_checksum(tempPackage)
    if(checksum != computedChecksum):
        print("Checksum missmatch!")
        return False

    return True

def print_raw(response):
    for i in range(4):
        shortLow = get_short_network(response, i*4)
        shortHight = get_short_network(response, i*4 + 2)
        lowString = "{0:b}".format(shortLow)
        highString = "{0:b}".format(shortHight)
        print(lowString, " ", highString)
