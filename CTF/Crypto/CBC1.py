from pwn import *
#使用debug模式，可以看到交互过程
#context.log_level = 'debug'

# 目标服务器的URL和端口
url = "127.0.0.1"
port = 60208

# 创建与目标服务器的连接
conn = remote(url, port)

# 加密消息的获得
encrypted_msg = conn.recvline()
print("加密消息:", encrypted_msg)
encrypted_msg=encrypted_msg.decode()

# 将加密消息转换为字节
encrypted_msg_bytes = bytes.fromhex(encrypted_msg)
print("加密消息字节:", encrypted_msg_bytes)

# 分离初始化向量和加密文本
IV = encrypted_msg_bytes[:16]
enc_msg = encrypted_msg_bytes[16:]

# 用于存储解密的中间值
intermediate_bytes = [0] * 16

# 逐字节破解,初始化iv=[0]*16，从最后一个字节开始，逐个字节破解，直到第一个字节，得到中间值
#当返回403时，说明有一位破解成功，记录中间值，继续破解下一位
#当返回200时，说明iv破解完成，记录中间值
iv = [0] * 16
for i in range(15, -1, -1):
    #将已确定的iv部分与填充字符个数进行异或，得到新的iv
    for k in range(15, i, -1):
        iv[k]=intermediate_bytes[k]^(16-i)
    for j in range(256):
        iv[i] = j
        conn.sendline((bytes(iv) + enc_msg[:16]).hex())
        result = conn.recvline().decode()
        if result == "403\n" or result == "200\n":
            intermediate_bytes[i] = j ^ (16-i)
            break
        if j == 255:
            print("error")
            exit()

#中间值和已知的IV做异或，则得到第一组密文的明文
plaintext1 = [0] * 16
ciphertext1 = enc_msg[:16]
print(ciphertext1)
for i in range(16):
    plaintext1[i] = intermediate_bytes[i] ^ IV[i]
#转成字符串输出
print("明文第一部分:", ''.join([chr(c) for c in plaintext1]))

iv = [0] * 16
enc_msg=enc_msg[16:]
intermediate_bytes = [0] * 16
for i in range(15, -1, -1):
    #将已确定的iv部分与填充字符个数进行异或，得到新的iv
    for k in range(15, i, -1):
        iv[k]=intermediate_bytes[k]^(16-i)
    for j in range(256):
        iv[i] = j
        conn.sendline((bytes(iv) + enc_msg[:16]).hex())
        result = conn.recvline().decode()
        if result == "403\n" or result == "200\n":
            intermediate_bytes[i] = j ^ (16-i)
            break
        if j == 255:
            print("error")
            exit()

plaintext2 = [0] * 16
ciphertext2 = enc_msg[:16]
print(intermediate_bytes)
for i in range(16):
    plaintext2[i] = intermediate_bytes[i] ^ ciphertext1[i]
#转成字符串输出
print("明文第二部分:", ''.join([chr(c) for c in plaintext2]))

iv = [0] * 16
enc_msg=enc_msg[16:]
intermediate_bytes = [0] * 16
for i in range(15, -1, -1):
    #将已确定的iv部分与填充字符个数进行异或，得到新的iv
    for k in range(15, i, -1):
        iv[k]=intermediate_bytes[k]^(16-i)
    for j in range(256):
        iv[i] = j
        conn.sendline((bytes(iv) + enc_msg[:16]).hex())
        result = conn.recvline().decode()
        if result == "403\n" or result == "200\n":
            intermediate_bytes[i] = j ^ (16-i)
            break
        if j == 255:
            print("error")
            exit()

plaintext3 = [0] * 16
ciphertext3 = enc_msg[:16]
print(intermediate_bytes)
for i in range(16):
    plaintext3[i] = intermediate_bytes[i] ^ ciphertext2[i]
#转成字符串输出
print("明文第三部分:", ''.join([chr(c) for c in plaintext3]))
#把明文合起来
print("全部明文：",''.join([chr(c) for c in plaintext1])+''.join([chr(c) for c in plaintext2])+''.join([chr(c) for c in plaintext3]))

# 关闭连接
conn.close()
