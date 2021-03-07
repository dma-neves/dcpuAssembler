# a*b program

# a
lod $0 ADR
str $23 [ADR]

# b
lod $1 ADR
str $5 [ADR]

# i
lod $2 ADR
str $0 [ADR]

# r (result)
lod $3 ADR
str $0 [ADR]

mult_start:

	# r = r+a
	lod $3 ADR
	lod [ADR] RA
	lod $0 ADR
	lod [ADR] RB
	add RA RB
	lod $3 ADR
	str ACR [ADR]

	# i++
	lod $2 ADR
	lod [ADR] RA
	inc RA
	str ACR [ADR]

	# i-b
	lod [ADR] RA
	lod $1 ADR
	lod [ADR] RB
	sub RA RB

	jmpn mult_start

lod $3 ADR
lod [ADR] RA
hlt