import random
from sympy import isprime, mod_inverse

# 生成大素数
def generate_large_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

# 密钥生成
def generate_keys(bits=1024):
    # 选择两个大素数 p 和 q
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    
    # 计算它们的乘积 n
    n = p * q
    
    # 计算欧拉函数 φ(n)
    phi = (p - 1) * (q - 1)
    
    # 选择一个公钥指数 e，通常选择 65537
    e = 65537
    
    # 计算私钥指数 d，使得 d 是 e 关于 φ(n) 的模反元素
    d = mod_inverse(e, phi)
    
    # 返回公钥 (e, n) 和私钥 (d, n)
    return (e, n), (d, n)

# 加密
def encrypt(public_key, plaintext):
    e, n = public_key
    
    # 将明文转换为整数 m
    m = int.from_bytes(plaintext.encode(), 'big')
    
    # 计算密文 c = m^e mod n
    c = pow(m, e, n)
    
    return c

# 解密
def decrypt(private_key, ciphertext):
    d, n = private_key
    
    # 计算明文整数 m = c^d mod n
    m = pow(ciphertext, d, n)
    
    # 将整数 m 转换回明文
    plaintext = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
    
    return plaintext

# 示例使用
public_key, private_key = generate_keys()
plaintext = "Hello, RSA!"

# 使用公钥加密明文
ciphertext = encrypt(public_key, plaintext)

# 使用私钥解密密文
decrypted_text = decrypt(private_key, ciphertext)

print("原文:", plaintext)
print("密文:", ciphertext)
print("解密后:", decrypted_text)