# n! program                                               

# n = 5
lod $0 ADR
str $5 [ADR]

# r (result)
lod $1 ADR
str $1 [ADR]

# cnt (counter)
lod $2 ADR
str $2 [ADR]

factorial_start:

    lod $2 ADR
    lod [ADR] RC

    # r = r*cnt

    # i (multiplication counter)
    lod $3 ADR
    str $0 [ADR]

    # mr (multiplication result)
    lod $4 ADR
    str $0 [ADR]

    mult_start:

        # mr = mr+r
        lod $4 ADR
        lod [ADR] RA
        lod $1 ADR
        lod [ADR] RB
        add RA RB
        lod $4 ADR
        str ACR [ADR]

        # i++
        lod $3 ADR
        lod [ADR] RA
        inc RA
        lod $3 ADR
        str ACR [ADR]

        # if(i - cnt < 0) goto mult_start
        lod $3 ADR
        lod [ADR] RA
        lod $2 ADR
        lod [ADR] RB
        sub RA RB
        jmpn mult_start

    lod $4 ADR
    lod [ADR] RA
    lod $1 ADR
    str RA [ADR]

    # cnt++
    lod $2 ADR
    lod [ADR] RA
    inc RA
    lod $2 ADR
    str ACR [ADR]

    # if(cnt - n <= 0) goto factorial_start
    lod $2 ADR
    lod [ADR] RA
    lod $0 ADR
    lod [ADR] RB
    sub RA RB
    jmpn factorial_start
    jmpz factorial_start

lod $1 ADR
lod [ADR] RA
hlt