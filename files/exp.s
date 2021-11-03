psh $2
psh $5
psh $9
psh $4
psh $2
psh $4
pop RB
pop RC
lod $0 RD
loop_start:
add RD RB
lod ACR RD
dec RC
jmpz loop_end
lod ACR RC
jmp loop_start
loop_end:
psh RD
pop RB
pop RC
add RB RC
lod ACR RB
psh RB
pop RB
pop RC
sub RB RC
lod ACR RB
psh RB
psh $3
pop RB
pop RC
sub RB RC
lod ACR RB
psh RB
pop RB
pop RC
add RB RC
lod ACR RB
psh RB
pop RB
pop RC
add RB RC
lod ACR RB
psh RB
hlt