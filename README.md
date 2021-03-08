# Assembler

**Description**
  - Assembler for my [8bit cpu](https://github.com/dma-neves/8bitCPU) written in python.
  - Given a .s file with assembly code, the assembler.py program generates a .binary file. A .binary is basically a text file with a bunch of strings containing '0's and '1's. The .binary file can then be used with the romGenerator.py program to generate the VHDL file for the 256 byte ROM the CPU uses.
  
**Syntax**
  - The [ISA](https://github.com/dma-neves/8bitCPU/blob/main/other/ISA.txt) of the cpu can be found in the VHDL_8bitCPU rep.
  - The only nuances the assembler contains are the usage of labels for the jump instructions instead of using the memory locations directly and the addition of comments using the "#" or ';' characters.
  
**Example**
  ![alt text](https://github.com/dma-neves/Assembler/blob/main/other/code.png)
