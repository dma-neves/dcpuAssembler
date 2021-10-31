import shutil
import sys
from vhdlCode import *

def romLine(i, inst):

    a = str(i)
    b = str(i-15)
    return "I(" + a + " downto " + b + ") <= \"" + inst + "\";\n"

# Get a string with the binary representation of n
def intTo8bitStr(n):

    bitStr = "{0:b}".format(n)
    missingZeros = 8 - len(bitStr)

    return '0'*missingZeros + bitStr

args = sys.argv

if len(args) != 2:
    print("usage: python3 assembler.py stringBinaryFile.strbinary")

else:

    """
    shutil.copy("other/ROM256_start.vhd", "files/ROM256.vhd")

    romf = open("files/ROM256.vhd", 'a')
    binf = open(args[1])

    i = 15
    lc = 0

    for inst in binf:

        romf.write( romLine(i, inst[:-1]) )

        i += 16
        lc += 1

    for j in range(lc+1, 129):

        romf.write( romLine(i, "0000000000000000") )
        i += 16

    romf.write("\nend Behavioral;")

    romf.close()
    binf.close()

    print("rom generated successfully")
    """

    romf = open("../files/ROM256.vhd", 'w+')
    binf = open(args[1])

    romf.write(start)

    c = 0
    for inst in binf:
        romf.write('            when \"' + intTo8bitStr(c) + '\" => DO <= \"' + inst[:-1] + '\";\n')
        c += 1

    #for i in range(c, 256):
    #    romf.write('            when \"' + intTo8bitStr(i) + '\" => DO <= \"00000000\";\n')

    romf.write(end)
    print("rom generated successfully")