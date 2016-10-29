## HELPER FUNCTIONS
# Help convert portions of strings (starting at pos) into integers of given size (in C)
# in network order


def get_byte(string, pos):
    return ord(string[pos])

def get_short_network(string, pos):
    return (ord(string[pos]) << 8) + ord(string[pos + 1])

def get_int_network(string, pos):
    sig1 = ord(string[pos]) << 24
    sig2 = ord(string[pos + 1]) << 16
    sig3 = ord(string[pos + 2]) << 8
    sig4 = ord(string[pos + 3])
    return sig1 + sig2 + sig3 + sig4


def ones_compliment_addition(x, y):
    c = x + y
    #           last 16b    get MSB and add
    return (c & 0xffff) + ((c & 0x10000) >> 16)


def get_checksum(string):
    result = 0

    # Iterate over every 16-byte range
    for i in range(0, len(string), 2):
        shortVar = get_short_network(string, i)
        result = ones_compliment_addition(result, shortVar)
    return ~result & 0xffff # The magic of bits
