from Crypto.Util.number import inverse, long_to_bytes
import gmpy2

# 步骤1: 读取output.txt中的n和c
with open("output.txt", "r") as f:
    lines = f.readlines()
    n = int(lines[0].strip().split(" = ")[1])
    c = int(lines[1].strip().split(" = ")[1])

# 步骤2: 使用Coppersmith方法找到p和q（这里简化处理，因为p和q非常接近）
# 注意：这里的实现依赖于p和q的特定属性，并不是一个通用的Coppersmith攻击实现
phi = n
for i in range(2, 1000000):
    if n % i == 0:
        p = i
        q = n // p
        phi = (p-1)*(q-1)
        break

# 步骤3: 计算私钥d并解密c
e = 65537
d = inverse(e, phi)
m = pow(c, d, n)

# 步骤4: 将m转换回原始flag
flag = long_to_bytes(m)
#转成字符串
flag = flag.decode()
print(flag)