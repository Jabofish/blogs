from pwn import *
from Crypto.Util.number import *
import hashlib
import itertools
import string
import gmpy2
#context.log_level = 'debug'
url = "10.214.160.13"
port = 12505
conn = remote(url, port)
powtext=conn.recvline().decode()
#接收格式示例：sha256(str).hexdigest()[-6:] == a51299
target_hash_suffix = powtext.split("== ")[1].strip()

def brute_force_sha256(target):
    chars = string.ascii_letters + string.digits
    for length in range(1, 10):
        for item in itertools.product(chars, repeat=length):
            s = ''.join(item)
            if hashlib.sha256(s.encode()).hexdigest()[-6:] == target:
                return s
    return None

result = brute_force_sha256(target_hash_suffix)
print(result)
conn.sendline(result)
'''
完成验证后进入正式交互，服务器返回：
Plaese choose one:
0. Description
1. Sign
2. Verify
3. Quit
'''

"""
def sign(m, d, n):
    return pow(bytes_to_long(m), d, n)
def verify(c, e, n):
    return 'Plz give me the flag!'  == long_to_bytes(pow(bytes_to_long(c), e, n))
"""
#正式做RSA-选择明密文攻击
conn.sendline(b"1")
conn.recvuntil(b'Give me the msg you want to sign in hex: ')
conn.sendline(b"0002")
conn.recvuntil(b'Here is your signature: ')
cipher1 = conn.recv().rstrip(b'\n')
cipher1 = int(cipher1.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"0004")
conn.recvuntil(b'Here is your signature: ')
cipher2 = conn.recvline()
cipher2 = int(cipher2.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"0003")
conn.recvuntil(b'Here is your signature: ')
cipher3 = conn.recvline()
cipher3 = int(cipher3.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"0009")
conn.recvuntil(b'Here is your signature: ')
cipher4 = conn.recvline()
cipher4 = int(cipher4.decode(), 16)

conn.sendline(b"1")
conn.sendline(b"0008")
conn.recvuntil(b'Here is your signature: ')
cipher6 = conn.recvline()
cipher6 = int(cipher6.decode(), 16)
n1=gmpy2.gcd(cipher1*cipher1-cipher2, cipher3*cipher3-cipher4)
#117539425503417846151799038508858073088368534710049 (51 digits) = 3 × 127 × 281 × 269323062708893 × 4076418121333894008279720561313 (31 digits)
factor1=3
factor2=127
factor3=281
factor4=269323062708893
factor5=4076418121333894008279720561313
factor1_hex=hex(factor1)[2:]
factor2_hex=hex(factor2)[2:]
factor3_hex=hex(factor3)[2:]
factor4_hex=hex(factor4)[2:]
factor5_hex=hex(factor5)[2:]
'''
#构造式子用的函数
i = 1
while True:
    try:
        # 计算factor的i倍对应的十六进制字符串，并尝试转换为ASCII码
        hex_str = hex(i * factor1*factor2*factor3*((factor4*17)//17)*((factor5*25745)//((25745*41)//41)))[2:]
        ascii_str = bytes.fromhex(hex_str).decode('ascii')
        print(f"倍数: {i}, 十六进制: {hex_str}, ASCII: {ascii_str}")
        break  # 成功转换后退出循环
    except ValueError:
        # 如果转换失败，增加i的值继续尝试
        i += 1
    except UnicodeDecodeError:
        # 如果转换的字符串不是有效的ASCII字符，增加i的值继续尝试
        i += 1
'''        
#factor4,倍数: 17, 十六进制: 10441d4134346d, ASCII: DA44m
#factor5,倍数: 25745, 十六进制: 14364e386075467d36105807696931, ASCII: 6N8`uF}6Xii1
#25745,倍数: 41, 十六进制: 101b39, ASCII:
#factor1*factor2*factor3*((factor4*17)/17)*((factor5*25745)/((25745*41)/41))
#117539425503417846151799038508858073088368534710049 (51 digits) = 3 × 127 × 281 × 269323062708893 × 4076418121333894008279720561313 (31 digits)
m='Plz give me the flag!'
conn.sendline(b"1")
conn.sendline(b"0003")
conn.recvuntil(b'Here is your signature: ')
factor1_cipher = conn.recvline()
factor1_cipher = int(factor1_cipher.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"007f")
conn.recvuntil(b'Here is your signature: ')
factor2_cipher = conn.recvline()
factor2_cipher = int(factor2_cipher.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"0119")
conn.recvuntil(b'Here is your signature: ')
factor3_cipher = conn.recvline()
factor3_cipher = int(factor3_cipher.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"10441d4134346d")
conn.recvuntil(b'Here is your signature: ')
factor4_cipher_1 = conn.recvline()
factor4_cipher_1 = int(factor4_cipher_1.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"0011")
conn.recvuntil(b'Here is your signature: ')
factor4_cipher_2 = conn.recvline()
factor4_cipher_2 = int(factor4_cipher_2.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"14364e386075467d36105807696931")
conn.recvuntil(b'Here is your signature: ')
factor5_cipher_1 = conn.recvline()
factor5_cipher_1 = int(factor5_cipher_1.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"101b39")
conn.recvuntil(b'Here is your signature: ')
factor5_cipher_2 = conn.recvline()
factor5_cipher_2 = int(factor5_cipher_2.decode(), 16)
conn.sendline(b"1")
conn.sendline(b"0029")
conn.recvuntil(b'Here is your signature: ')
factor5_cipher_3 = conn.recvline()
factor5_cipher_3 = int(factor5_cipher_3.decode(), 16)
key=(factor1_cipher*factor2_cipher*factor3_cipher*factor4_cipher_1*inverse(factor4_cipher_2%n1,n1)*factor5_cipher_1*inverse((factor5_cipher_2*inverse(factor5_cipher_3%n1,n1))%n1,n1))%n1
conn.sendline(b"2")
conn.recvuntil(b'Give me the signature you want to verify in hex: ')
conn.sendline(hex(key)[2:])
print(conn.recv())
conn.close()