import random
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def generate_prime_candidate(length):
    p = 0
    while not is_prime(p) or p < 4:
        p = random.randint(2**(length-1), 2**length - 1)
    return p

def main():
    random.seed()
    choice = int(input("如果手动输入素数请按输入：1, 自动生成素数请输入：2\n"))

    if choice == 1:
        p = int(input("请输入一个素数 p：\n"))
        if is_prime(p):
            print(f"{p} 是素数")
        else:
            print(f"{p} 不是素数")
            return
    else:
        p = generate_prime_candidate(8)
        print(f"生成的素数为：{p}")

    g = int(input("请输入一个小于 p 的随机数 g：\n"))
    x = int(input("请输入一个小于 p 的随机数 x：\n"))

    y = mod_exp(g, x, p)

    k = 0
    while gcd(k, p-1) != 1:
        k = random.randint(2, p-1)

    print(f"公钥 y, g, p 和私钥 x 分别是：{y}, {g}, {p}, {x}")

    m = int(input("请输入明文：\n"))

    c1 = mod_exp(g, k, p)
    c2 = (m * mod_exp(y, k, p)) % p

    print(f"加密后密文是：{c1}, {c2}")

    c1 = int(input("请输入密文 c1：\n"))
    c2 = int(input("请输入密文 c2：\n"))

    d = mod_exp(c1, x, p)
    decrypted_m = (c2 * mod_exp(d, p-2, p)) % p

    print(f"解密后明文是：{decrypted_m}")

if __name__ == "__main__":
    main()