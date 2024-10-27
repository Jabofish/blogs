result = b'\xfc\xf2\x1dE\xf7\xd8\xf7\x1e\xed\xccQ\x8b9:z\xb5\xc7\xca\xea\xcd\xb4b\xdd\xcb\xf2\x939\x0b\xec\xf2'
RT = matrix(Zmod(256), 3, 10)
for p in range(3):
    for q in range(10):
        RT[p, q] = result[p + q * 3]
for a in range(256):
    print(f'Line:{a}')
    for b in range(256):
        for c in range(256):
            MT_inv = matrix(Zmod(256), [[a, b, c], [0,0,0], [0, 0, 0]]) 
            FT_decrypted = MT_inv * RT
            flag_decrypted = ''.join(chr(int(x)) for x in FT_decrypted.list())
            if all(32 <= ord(char) <= 126 or ord(char)==0 for char in flag_decrypted) and flag_decrypted[0] == 'A' and flag_decrypted[1] == '{':
                print(f"找到可能的解密结果: {flag_decrypted}", a, b, c)
print("程序执行完成。")

result = b'\xfc\xf2\x1dE\xf7\xd8\xf7\x1e\xed\xccQ\x8b9:z\xb5\xc7\xca\xea\xcd\xb4b\xdd\xcb\xf2\x939\x0b\xec\xf2'
RT = matrix(Zmod(256), 3, 10)
for p in range(3):
    for q in range(10):
        RT[p, q] = result[p + q * 3]
for a in range(256):
    print(f'Line:{a}')
    for b in range(256):
        for c in range(256):
            MT_inv = matrix(Zmod(256), [[124, 177, 43], [a, b, c], [0, 0, 0]]) 
            FT_decrypted = MT_inv * RT
            flag_decrypted = ''.join(chr(int(x)) for x in FT_decrypted.list())
            if all(32 <= ord(char) <= 126 or ord(char)==0 for char in flag_decrypted) and flag_decrypted[10] == 'A':
                print(f"找到可能的解密结果: {flag_decrypted}", a, b, c)
print("程序执行完成。")

result = b'\xfc\xf2\x1dE\xf7\xd8\xf7\x1e\xed\xccQ\x8b9:z\xb5\xc7\xca\xea\xcd\xb4b\xdd\xcb\xf2\x939\x0b\xec\xf2'
RT = matrix(Zmod(256), 3, 10)
for p in range(3):
    for q in range(10):
        RT[p, q] = result[p + q * 3]
for a in range(256):
    print(f'Line:{a}')
    for b in range(256):
        for c in range(256):
            MT_inv = matrix(Zmod(256), [[124, 177, 43], [157 ,38,157], [a, b, c]]) 
            FT_decrypted = MT_inv * RT
            flag_decrypted = ''.join(chr(int(x)) for x in FT_decrypted.list())
            if all(32 <= ord(char) <= 126 for char in flag_decrypted) and flag_decrypted[29] == '}' and flag_decrypted[20]=='A':
                print(f"找到可能的解密结果: {flag_decrypted}", a, b, c)
print("程序执行完成。")