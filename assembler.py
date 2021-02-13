import sys

instValue = {
    'addRARB' : 0,
    'addRARC' : 1,
    'addRA$X' : 2,
    'subRARB' : 3,
    'subRARC' : 4,
    'subRA$X' : 5,
    'incRA' : 6,
    'decRA' : 7,
    'negRA' : 8,
    'notRA' : 9,
    'andRARB' : 10,
    'andRARC' : 11,
    'orRARB' : 12,
    'orRARC': 13,

    'lodadrRA' : 14,
    'strRAadr' : 15,
    'lodadrRB' : 16,
    'strRBadr' : 17,
    'lodadrRC' : 18,
    'strRBadr' : 19,
    'lodACRRA' : 20,
    'strACRadr' : 21,
    'lod$XRA' : 22,

    'jmpadr' : 23,
    'jmpzadr' : 24,
    'jmpnadr' : 25,
    'jmpoadr' : 26,
    'hlt' : 27
    }

def intTo8bitStr(n):

    bitStr = "{0:b}".format(n)
    missingZeros = 8 - len(bitStr)

    return '0'*missingZeros + bitStr

def printError(lc):

    print("syntax error: line " + str(lc))
    quit()

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
        tokens = line.split()

        # Check if the line isnt empty or a comment line
        if len(tokens) != 0 and tokens[0][0] != "#" and tokens[0][0] != ";":

            # Check if line is label for jump instruction
            if tokens[-1][-1] == ':':
                if len(tokens) == 1:
                    label = tokens[0][:-1]
                    # Memory value for the jump instruction using this label will be the current instruction - 1
                    # sinse after executing the jump, the IC is incremented
                    labels[label] = ic-1
                else:
                    printError(lc)
            else:
                ic += 2
                instStr = ""
                data = 0
                
                for t in tokens:
                    
                    token_wd = t.replace('$', '') # Token without dollar

                    # If token is a numeric valuel, attribute it to the instruction data
                    if token_wd.isnumeric():
                        data = int(token_wd)
                        if '$' in t:
                            instStr += '$X'
                        else:
                            instStr += 'adr'
                    # If token is a label, attribute the correct memory address to the instruction data
                    elif t in labels:
                        data = labels[t]
                        instStr += 'adr'
                    else:
                        instStr += t

                # Check for invalid instruction
                if not (instStr in instValue):
                    printError(lc)

                inst = instValue[instStr]
                b = intTo8bitStr(data) + intTo8bitStr(inst)
                # Add instruction to the list
                instructions.append(b)

    f.close()
    # Write instructions to the binary file
    f = open(codeFile.replace(".s", ".binary"), 'w')
    for i in instructions:
        f.write(i)
        f.write("\n")

    f.close()

    print("successful assembly")