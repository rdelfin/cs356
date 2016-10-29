import random

address = "paris.cs.utexas.edu"
port = 35605
random.seed()

# M F     356         Lab #     Version
# 0 0 00000101100100 00000001  00000111

#          Client cookie
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#          Request Data (SSN)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#    Checksum      O     Result
# %%%%%%%%%%%%%%%% % %%%%%%%%%%%%%%%

mType = 0;
flag = 0;
coursenum = 356
labNumber = 0x1
version = 0x7
cookie = random.randint(0, 2147483647)
