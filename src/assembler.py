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

    'lod$XRA' : 14,
    'lod$XRB' : 15,
    'lod$XRC' : 16,
    'lod$XADR' : 17,

    'str$X[ADR]' : 18,
    'lod[X]ADR' : 19,

    'lod[ADR]RA' : 20,
    'strRA[ADR]' : 21,
    'lod[ADR]RB' : 22,
    'strRB[ADR]' : 23,
    'lod[ADR]RC' : 24,
    'strRC[ADR]' : 25,

    'lodACRRA' : 26,
    'lodACRADR' : 27,
    'strACR[ADR]' : 28,

    'strIC[ADR]' : 29,

    'jmpADR' : 30,
    'jmpX' : 31,
    'jmpzX' : 32,
    'jmpnX' : 33,
    'jmpoX' : 34,
    'hlt' : 35
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
                instExp = "" # Instruction expression
                data = 0
                
                for t in tokens:
                    
                    token_ws = t.replace('$', '').replace('[', '').replace(']', '') # Token without symbols

                    # If token is a numeric valuel, attribute it to the instruction data
                    if token_ws.isnumeric():
                        data = int(token_ws)
                        if '$' in t:
                            instExp += '$X'
                        elif '[' in t:
                            instExp += '[X]'
                        else:
                            instExp += 'X'
                    # If token is a label, attribute the correct memory address to the instruction data
                    elif t in labels:
                        data = labels[t]
                        instExp += 'X'
                    else:
                        instExp += t

                # Check for invalid instruction
                if not (instExp in instValue):
                    printError(lc)

                inst = instValue[instExp]
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