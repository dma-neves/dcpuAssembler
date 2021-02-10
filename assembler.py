import sys

def printError(lc):

    print("syntax error: line " + str(lc))
    quit()

def intTo8bitStr(n):
    bitStr = "{0:b}".format(n)
    missingZeros = 8 - len(bitStr)

    return '0'*missingZeros + bitStr

args = sys.argv

if len(args) != 2:
    print("usage: python3 assembler.py codeFile.s")

else:
    codeFile = args[1]
    print("assembling: " + codeFile)

    lc = 0 # line counter
    ic = 0 # instruction counter
    labels = {}
    instructions = []

    f = open(codeFile,'r')
    
    for line in f:

        lc += 1
        words = line.split()
        if len(words) != 0 and words[0][0] != '#':

            data = ""
            inst = ""

            if words[0] == "add":
                if len(words) != 3:
                    printError(lc)
                
                if words[1] == "RA" and words[2] == "RB":
                    data = "00000000"
                    inst = "00000000"
                
                elif words[1] == "RA" and words[2] == "RC":
                    data = "00000000"
                    inst = "00000001"

                elif words[1] == "RA" and words[3][0] == '$':
                    data = intTo8bitStr( int( words[3][1:] ) )
                    inst = "00000010"

                else:
                    printError(lc)

            elif words[0] == "sub":
                if len(words) != 3:
                    printError(lc)
                
                if words[1] == "RA" and words[2] == "RB":
                    data = "00000000"
                    inst = "00000011"
                
                elif words[1] == "RA" and words[2] == "RC":
                    data = "00000000"
                    inst = "00000100"

                elif words[1] == "RA" and words[3][0] == '$':
                    data = intTo8bitStr( int( words[3][1:] ) )
                    inst = "00000101"

                else:
                    printError(lc)

            elif words[0] == "inc":
                if len(words) != 2:
                    printError(lc)

                if words[1] == "RA":
                    data = "00000000"
                    inst = "00000110"

                else:
                    printError(lc)

            elif words[0] == "dec":
                if len(words) != 2:
                    printError(lc)

                if words[1] == "RA":
                    data = "00000000"
                    inst = "00000111"

                else:
                    printError(lc)

            elif words[0] == "neg":
                if len(words) != 2:
                    printError(lc)

                if words[1] == "RA":
                    data = "00000000"
                    inst = "00001000"

                else:
                    printError(lc)

            elif words[0] == "not":
                if len(words) != 2:
                    printError(lc)

                if words[1] == "RA":
                    data = "00000000"
                    inst = "00001001"

                else:
                    printError(lc)

            elif words[0] == "and":
                if len(words) != 3:
                    printError(lc)
                
                if words[1] == "RA" and words[2] == "RB":
                    data = "00000000"
                    inst = "00001010"
                
                elif words[1] == "RA" and words[2] == "RC":
                    data = "00000000"
                    inst = "00001011"

                else:
                    printError(lc)

            elif words[0] == "or":
                if len(words) != 3:
                    printError(lc)
                
                if words[1] == "RA" and words[2] == "RB":
                    data = "00000000"
                    inst = "00001100"
                
                elif words[1] == "RA" and words[2] == "RC":
                    data = "00000000"
                    inst = "00001101"

                else:
                    printError(lc)

            elif words[0] == "lod":
                if len(words) != 3:
                    printError(lc)

                if words[1] == "ACR" and words[2] == "RA":
                    data = "00000000"
                    inst = "00010100"

                elif words[1][0] == '$' and words[2] == "RA":
                    data = intTo8bitStr( int( words[1][1:] ) )
                    inst = "00010110"
                
                else:
                    data = intTo8bitStr( int( words[1] ) )

                    if words[2] == "RA":
                        inst = "00001110"

                    elif words[2] == "RB":
                        inst = "00010000"

                    elif words[2] == "RC":
                        inst = "00010010"

                    else:
                        printError(lc)

            elif words[0] == "str":
                if len(words) != 3:
                    printError(lc)

                data = intTo8bitStr( int( words[2] ) )

                if words[1] == "ACR":
                    inst = "00010101"

                elif words[1] == "RA":
                    inst = "00001111"

                elif words[1] == "RB":
                    inst = "00010001"

                elif words[1] == "RC":
                    inst = "00010011"
                
                else:
                    printError(lc)

            elif words[0] == "jmp":
                if len(words) != 2:
                    printError(lc)

                data = labels[words[1]]
                inst = "00010111"

            elif words[0] == "jmpz":
                if len(words) != 2:
                    printError(lc)

                data = labels[words[1]] 
                inst = "00011000"

            elif words[0] == "jmpn":
                if len(words) != 2:
                    printError(lc)

                data = labels[words[1]]
                inst = "00011001"
                
            elif words[0] == "jmpo":
                if len(words) != 2:
                    printError(lc)

                data = labels[words[1]]
                inst = "00011010"

            elif words[0] == "hlt":
                data = "00000000"
                inst = "00011011"

            elif words[0][-1] == ':':
                label = words[0][:-1]
                labels[label] = intTo8bitStr(ic-1)

            else:
                printError(lc)
            
            if words[0][-1] != ':':
                instructions.append(data + inst)
                ic += 2

    f.close()

    f = open(codeFile.replace(".s", ".binary"), 'w')

    for i in instructions:
        f.write(i)
        f.write("\n")

    f.close()

    print("successful assembly")