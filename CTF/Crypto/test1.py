m='Plz give me the flag!'
m_long=int(m.encode().hex(), 16)
print(m_long)
m=m_long.to_bytes((m_long.bit_length() + 7) // 8, 'big').decode()
print(m)
"""
def sign(m, d, n):
    return pow(bytes_to_long(m), d, n)
def verify(c, e, n):
    return 'Plz give me the flag!'  == long_to_bytes(pow(bytes_to_long(c), e, n))
"""
def find_factors(n):
    # 从最小的可能的因数开始
    for i in range(2, int(n**0.5) + 1):
        # 如果i是n的因数
        if n % i == 0:
            return i, n // i
    return None, None
#117539425503417846151799038508858073088368534710049 (51 digits) = 3 × 127 × 281 × 269323062708893 × 4076418121333894008279720561313 (31 digits)
factor1=3
factor2=127
factor3=281
factor4=269323062708893
factor5=4076418121333894008279720561313
#m_long=117539425503417846151799038508858073088368534710049
#把factor转换成hex
factor1_hex=hex(factor1)[2:]
factor2_hex=hex(factor2)[2:]
factor3_hex=hex(factor3)[2:]
factor4_hex=hex(factor4)[2:]
factor5_hex=hex(factor5)[2:]
#把factor_hex输出
#ASCII码的范围是0x00-0x7f
'''
print(factor1_hex)#3
print(factor2_hex)#7f
print(factor3_hex)#119
print(factor4_hex)#f4f2a97b8a9d
print(factor5_hex)#33739e09e3796d57c0ebb48aa1
print(hex(factor1*factor4)[2:])#2ded7fc729fd7
print(hex(factor2*factor4)[2:])#7984621449c3e3
print(hex(factor3*factor4)[2:])#10cde5c089b2655
print(hex(factor1*factor2*factor4)[2:])#16c8d263cdd4ba9
print(hex(factor1*factor3*factor4)[2:])#3269b1419d172ff
print(hex(factor2*factor3*factor4)[2:])#85624fa844f8042b
print(hex(factor1*factor2*factor3*factor4)[2:])#19026eef8cee80c81
print(hex(factor4*factor5)[2:])#313af7fcf9e61c05b60b74d374bfd4c4cecebd
print(hex(factor1*factor5)[2:])#9a5ada1daa6c480742c31d9fe3
print(hex(factor2*factor5)[2:])#19865b66e7d93d3e88b4ee90c5df
from itertools import combinations
'''
"""
from itertools import combinations
factors = [factor1, factor2, factor3, factor4, factor5]

# 生成并打印所有组合的十六进制乘积
for r in range(1, len(factors) + 1):
    for combo in combinations(factors, r):
        product = 1
        for factor in combo:
            product *= factor
        print(hex(product)[2:])
"""

"""
3
7f
119
x f4f2a97b8a9d
x 33739e09e3796d57c0ebb48aa1
17d
34b
x 2ded7fc729fd7
x 9a5ada1daa6c480742c31d9fe3
x 8b67
x 7984621449c3e3
x 19865b66e7d93d3e88b4ee90c5df 
x 10cde5c089b2655
x 3879e878dab0490552c2b92c2ab9
x 313af7fcf9e61c05b60b74d374bfd4c4cecebd
x 1a235
x 16c8d263cdd4ba9
x 4c931234b78bb7bb9a1ecbb2519d
x 3269b1419d172ff
x a96db96a9010db0ff8482b84802b
x 93b0e7f6edb2541122225e7a5e3f7e4e6c6c37
x 85624fa844f8042b
x 1c047a53f47d7439a40e99dce931c7
x 186c41067ff927e6d54faef4e6eb2a8da2988fc3
x 3609ba34ae4d94c244d2933c1b26908c0700ed75
x 19026eef8cee80c81
x 540d6efbdd785cacec2bcd96bb9555
x 4944c3137feb77b47fef0cdeb4c17fa8e7c9af49
x a21d2e9e0ae8be46ce77b9b45173b1a41502c85f
x 1aced36022787ccc6024770ad17821b5777975cd0b
506c7a2067697665206d652074686520666c616721
"""
#print(bytes.fromhex('506c7a2067697665206d652074686520666c616721').decode())
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
        
#factor4,倍数: 17, 十六进制: 10441d4134346d, ASCII: DA44m
#factor5,倍数: 25745, 十六进制: 14364e386075467d36105807696931, ASCII: 6N8`uF}6Xii1
#25745,倍数: 41, 十六进制: 101b39, ASCII:
#factor1*factor2*factor3*((factor4*17)/17)*((factor5*25745)/((25745*41)/41))
#117539425503417846151799038508858073088368534710049 (51 digits) = 3 × 127 × 281 × 269323062708893 × 4076418121333894008279720561313 (31 digits)
factor1=3
factor2=127
factor3=281
factor4=269323062708893
factor5=4076418121333894008279720561313
factor1*factor2*factor3*((factor4*0x11)//0x11)*((factor5*25745)//((25745*0x29)//0x29))
from Crypto.Util.number import *
print(inverse(269323062708893,4076418121333894008279720561313))