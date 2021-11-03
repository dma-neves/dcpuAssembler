#!/usr/bin/env python3

import sys
from isa import *

# Get the value/number of a given register or -1 if the token is invalid
def getRegisterVal(token):

    if token == 'sp':
        return 7

    elif len(token) == 2 and token[0] == 'r':
        return ord(token[1]) - ord('a')

    return -1

# Get a string with the binary representation of n
def intTo16bitStr(n):

    bitStr = "{0:b}".format(n)
    missingZeros = 16 - len(bitStr)

    return '0'*missingZeros + bitStr

def printError(line):

    print("syntax error: " + str(line))
    quit()

# Replace macros by the corresponding instructions
def resolveMacros(lines):
    
    newLines = []

    for line in lines:
        tokens = line.lower().split(' ')

        if tokens[0] == 'psh':
            val = tokens[1]
            newLines.append('lod SP ADR')
            newLines.append('str ' + val + ' [ADR]')
            newLines.append('inc SP')
            newLines.append('lod ACR SP')

        elif tokens[0] == 'pop':

            if len(tokens) == 1:
                newLines.append('dec SP')
                newLines.append('lod ACR SP')

            else:
                reg = tokens[1]
                newLines.append('dec SP')
                newLines.append('lod ACR SP')
                newLines.append('lod SP ADR')
                newLines.append('lod [ADR] ' + reg)

        elif tokens[0] == 'lsr':
            pos = tokens[1]
            reg = tokens[2]
            newLines.append('ssp ' + pos)
            newLines.append('lod ACR ADR')
            newLines.append('lod [ADR] ' + reg)

        elif tokens[0] == 'srs':
            reg = tokens[1]
            pos = tokens[2]
            newLines.append('ssp ' + pos)
            newLines.append('lod ACR ADR')
            newLines.append('str ' + reg + ' [ADR]')

        elif tokens[0] == 'lod' and tokens[1][0] == '$' and (tokens[2][0] == 'r' or tokens[2] == "sp"):
            val = tokens[1]
            reg = tokens[2]
            newLines.append('lod $62 ADR')
            newLines.append('str ' + val + ' [ADR]')
            newLines.append('lod [ADR] ' + reg)

        else:
            newLines.append(line)

    return newLines

# Remove empty lines and comments
def removeUnnecessaryLines(lines):

    newLines = []

    for line in lines:
        if line.strip() and not ('#' in line or ';' in line):
            newLines.append(line.strip())

    return newLines

# Return all the executable instructions and a map with the memory addresses of each label
def resolveLabels(lines):

    ic = 0
    labels = {}
    instructions = []

    for line in lines:
        tokens = line.lower().split(' ')

        # Check if line is label for jump instruction
        if tokens[-1][-1] == ':':
            if len(tokens) == 1:
                label = tokens[0][:-1].lower()
                # Memory value for the jump instruction using this label will be the current instruction - 1
                # sinse after executing the jump, the IC is incremented
                labels[label] = ic-1
            else:
                printError(line)
        else:
            instructions.append(line)
            ic += 2

    return instructions, labels

def main():
    args = sys.argv

    if len(args) < 3:
        print("usage: python3 assembler.py codeFile.s outputDataType")
        print("outputDataType can be b (binary) or s (string)")

    else:
        codeFile = args[1]
        dataType = args[2]
        printInstructions = False

        if len(args) == 4 and args[3] == "-p":
            printInstructions = True


        print("assembling: " + codeFile)

        binaryInstructions = []
        f = open(codeFile, 'r')
        lines = resolveMacros( removeUnnecessaryLines(f) )
        instructions, labels = resolveLabels(lines)
        
        counter = 0
        for instruction in instructions:
            tokens = instruction.lower().split(' ')
            instExp = "" # Instruction expression
            data = 0
            
            for t in tokens:

                if t == ";" or t == "#":
                    break

                reg = getRegisterVal(t)

                # If token is a register, attribute the register value to the instruction data
                if reg != -1:

                    if "rx" in instExp:
                        data = data + (reg << 8)
                        instExp += "ry"

                    else:
                        data = reg
                        instExp += "rx"
                
                # If token is a numeric valuel, attribute it to the instruction data
                elif '$' in t:
                    data = int(t.replace('$', ''))
                    instExp += '$v'

                # If token is a label, attribute the correct memory address to the instruction data
                elif t in labels:
                    data = labels[t]
                    instExp += ('x' if 'jmp' in instruction.lower() else '$v')

                else:
                    instExp += t

            # Check for invalid instruction
            if not (instExp in instValue):
                print(instruction)
                printError(instExp)

            inst = instValue[instExp]

            if dataType == 's':
                binaryInstructions.append(intTo16bitStr(inst))
                binaryInstructions.append(intTo16bitStr(data))
                # print(instExp + " " + str(data))

            else:
                binaryInstructions.append(inst)
                binaryInstructions.append(data)

            if printInstructions:
                print(instruction + " (inst: " + str(inst) + " data: " + str(data) + " address: " + str(counter) + ")")
                counter += 2

        f.close()

        # Write instructions to the binary file
        if dataType == 's':
            f = open(codeFile.replace(".s", ".strbinary"), 'w')
            for i in binaryInstructions:
                f.write(i)
                f.write("\n")

        else:
            f = open(codeFile.replace(".s", ".binary"), 'w+b')
            f.write(bytearray(binaryInstructions))

        f.close()
        print("successful assembly")

main()