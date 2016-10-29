# Courtesy of http://stackoverflow.com/a/29843639
MOD = 1 << 16
def ones_comp_add16(num1,num2):
    result = num1 + num2
    return result if result < MOD else (result+1) % MOD

def get_byte(string, pos):
    return ord(string[pos])

def get_short_network(string, pos):
    return ord((string[pos]) << 8) + ord(string[pos + 1])

def get_int_network(string, pos):
    sig1 = ord(string[pos]) << 24
    sig2 = ord(string[pos + 1]) << 16
    sig3 = ord(string[pos + 2]) << 8
    sig4 = ord(string[pos + 3])
    return sig1 + sig2 + sig3 + sig4
