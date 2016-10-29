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


# Courtesy of http://stackoverflow.com/a/1769267
def carry_around_add(a, b):
    c = a + b
    #           last 16b    get MSB and add
    return (c & 0xffff) + ((c & 0x10000) >> 16)

def get_checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = get_short_network(msg, i)
        s = carry_around_add(s, w)
    return ~s & 0xffff
