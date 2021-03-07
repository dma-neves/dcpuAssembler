all:
	gcc -o assmb assembler.c

run: all
	./assmb files/multiply.s
