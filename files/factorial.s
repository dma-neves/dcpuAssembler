; n! program

; n = 5
lod $5 RA
str RA 0

; r (result)
lod $1 RA
str RA 1

; cnt (counter)
lod $2 RA
str RA 2

factorial_start:

    lod 2 RC

    ; r = r*cnt

    ; i (multiplication counter)
    lod $0 RA
    str RA 3

    ; mr (multiplication result)
    lod $0 RA
    str RA 4

    mult_start:

        ; mr = mr+r
        lod 4 RA
        lod 1 RB
        add RA RB
        str ACR 4

        ; i++
        lod 3 RA
        inc RA
        str ACR 3

        ; if(i - cnt < 0) goto mult_start
        lod 3 RA
        lod 2 RB
        sub RA RB
        jmpn mult_start

    lod 4 RA
    str RA 1

    ; cnt++
    lod 2 RA
    inc RA
    str ACR 2

    ; if(cnt - n <= 0) goto factorial_start
    lod 2 RA
    lod 0 RB
    sub RA RB
    jmpn factorial_start
    jmpz factorial_start

lod 1 RA
hlt