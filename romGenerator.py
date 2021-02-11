import shutil
import sys

def romLine(i, inst):

    a = str(i)
    b = str(i-15)
    return "I(" + a + " downto " + b + ") <= \"" + inst + "\";\n"

args = sys.argv

if len(args) != 2:
    print("usage: python3 assembler.py binaryFile.binary")

else:

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

