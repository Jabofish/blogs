"""
.data:00000000006BA100 c0              db 72h, 71h, 65h, 76h, 4Ch, 75h, 54h, 5Ah
.data:00000000006BA100                                         ; DATA XREF: main+A7↑o
.data:00000000006BA108                 db 64h
.data:00000000006BA109                 db  43h ; C
.data:00000000006BA10A                 db  56h ; V
.data:00000000006BA10B                 db  4Dh ; M
.data:00000000006BA10C                 db  60h ; `
.data:00000000006BA10D                 db  58h ; X
.data:00000000006BA10E                 db  54h ; T
.data:00000000006BA10F                 db  52h ; R
.data:00000000006BA110                 db  47h ; G
.data:00000000006BA111                 db  7Dh ; }
.data:00000000006BA112                 db  55h ; U
.data:00000000006BA113                 db  48h ; H
.data:00000000006BA114                 db  42h ; B
.data:00000000006BA115                 db  79h ; y
.data:00000000006BA116                 db  51h ; Q
.data:00000000006BA117                 db  56h ; V
.data:00000000006BA118                 db  5Eh ; ^
.data:00000000006BA119                 db  4Fh ; O
.data:00000000006BA11A                 db  76h ; v
.data:00000000006BA11B                 db  4Eh ; N
.data:00000000006BA11C                 db  43h ; C
.data:00000000006BA11D                 db  4Fh ; O
.data:00000000006BA11E                 db  4Ah ; J
.data:00000000006BA11F                 db  13h
.data:00000000006BA120                 db  6Eh ; n
.data:00000000006BA121                 db    0
.data:00000000006BA122                 db    0
.data:00000000006BA123                 db    0
.data:00000000006BA124                 db    0
.data:00000000006BA125                 db    0
.data:00000000006BA126                 db    0
.data:00000000006BA127                 db    0
.data:00000000006BA128                 db    0
.data:00000000006BA129                 db    0
.data:00000000006BA12A                 db    0
.data:00000000006BA12B                 db    0
.data:00000000006BA12C                 db    0
.data:00000000006BA12D                 db    0
.data:00000000006BA12E                 db    0
.data:00000000006BA12F                 db    0
.data:00000000006BA130                 db    0
.data:00000000006BA131                 db    0
.data:00000000006BA132                 db    0
.data:00000000006BA133                 db    0
.data:00000000006BA134                 db    0
.data:00000000006BA135                 db    0
.data:00000000006BA136                 db    0
.data:00000000006BA137                 db    0
.data:00000000006BA138                 db    0
.data:00000000006BA139                 db    0
.data:00000000006BA13A                 db    0
.data:00000000006BA13B                 db    0
.data:00000000006BA13C                 db    0
.data:00000000006BA13D                 db    0
.data:00000000006BA13E                 db    0
.data:00000000006BA13F                 db    0
"""


flag = [0x72, 0x71, 0x65, 0x76, 0x4C, 0x75, 0x54, 0x5A, 0x64, 0x43, 0x56, 0x4D, 0x60, 0x58, 0x54, 0x52, 0x47, 0x7D, 0x55, 0x48, 0x42, 0x79, 0x51, 0x56, 0x5E, 0x4F, 0x76, 0x4E, 0x43, 0x4F, 0x4A, 0x13, 0x6E]
data = []
for j in range(len(flag)):
    for i in range(0x20, 0x7f):
        if (i ^ j ^ 0x33) == flag[j]:
           original_value = i
           break
    data.append(chr(original_value))
print("flag=", ''.join(data))

encoded_str = "OSLSPlrSYBDxVxDxV0Dqa07dWT7EKErjV0XqWUb7"
Base64list = '-*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
decoded_str = ''
for i, char in enumerate(encoded_str):
    index = Base64list.find(char)
    new_index = (index - i) % len(Base64list)
    new_char = Base64list[new_index]
    decoded_str += new_char

print(decoded_str)