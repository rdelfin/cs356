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

# Creates a request string based on data and cookies
def package_request(requestData, clientCookie):
    # Default values for multiple parts
    header = 356
    labN = 1
    version  = 7
    checksum = 0
    result = 0

    # Pack according to the C struct tefined at top of page
    tempPackage  = struct.pack('!HBBIIHH', header, labN, version, clientCookie, requestData, checksum, result)

    # Compute the checksum
    checksum = get_checksum(tempPackage)

    # Repackage with checksum included and return
    return struct.pack('!HBBIIHH', header, labN, version, clientCookie, requestData, checksum, result)

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

def get_result(response):
    data = struct.unpack('!HBBIIHH', response)
    result = data[6]
    return result & 0x7fff

def print_raw(response):
    for i in range(4):
        shortLow = get_short_network(response, i*4)
        shortHight = get_short_network(response, i*4 + 2)
        lowString = "{0:b}".format(shortLow)
        highString = "{0:b}".format(shortHight)
        print(lowString, " ", highString)
