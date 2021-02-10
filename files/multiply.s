# a*b program

# a
lod $23 RA
str RA 0

# b
lod $5 RA
str RA 1

# i
lod $0 RA
str RA 2

# r (result)
lod $0 RA
str RA 3

mult_start:

	# r = r+a
	lod 3 RA
	lod 0 RB
	add RA RB
	str ACR 3

	# i++
	lod 2 RA
	inc RA
	str ACR 2

	#i-b
	lod 2 RA
	lod 1 RB
	sub RA RB

	jmpn mult_start

lod 3 RA
hlt