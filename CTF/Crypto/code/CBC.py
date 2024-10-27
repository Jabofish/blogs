# 假设的原始明文和目标明文
original_plaintext = b"Welcome to SECUR"+b"E Crypto System\n"+b"No way to hack\xf0\x9f\x98\x9c"
target_plaintext =   b"Your Crypto Syst"+b"em is HACKED BY "+b"AAA\xF0\x9F\xA4\xA3\xF0\x9F\xA4\xA3\xF0\x9F\xA4\xA3\x01\x01\x01"
ciphertext = '504a17a9a1135ee44382748a211a388744ce2fbbaed197df312777c88980d5212570ad9a66fe373b8de7fb0fe0225835524a4758bcace1a2521f153c29caada6ae999061ecf74e587a97073fd5c9e9b0'
ciphertext = bytes.fromhex(ciphertext)

original_iv = ciphertext[:16]
change_for_first_block = bytes([original_plaintext[i] ^ target_plaintext[i] for i in range(16)])
modified_iv = bytes([original_iv[i] ^ change_for_first_block[i] for i in range(16)])

original_first_ciphertext_block = ciphertext[16:32]
change_for_second_block = bytes([original_plaintext[i] ^ target_plaintext[i] for i in range(16, 32)])
modified_first_ciphertext_block = bytes([original_first_ciphertext_block[i-16] ^ change_for_second_block[i-16] for i in range(16, 32)])
new_ciphertext = modified_iv + modified_first_ciphertext_block + ciphertext[32:]

original_second_ciphertext_block = ciphertext[32:48]
change_for_third_block = bytes([original_plaintext[i] ^ target_plaintext[i] for i in range(32, 48)])
modified_second_ciphertext_block = bytes([original_second_ciphertext_block[i-32] ^ change_for_third_block[i-32] for i in range(32, 48)])
new_ciphertext = new_ciphertext[:32] + modified_second_ciphertext_block + ciphertext[48:]

original_third_ciphertext_block = ciphertext[48:50]
change_for_fourth_block = bytes([original_plaintext[i] ^ target_plaintext[i] for i in range(48, 50)])
modified_third_ciphertext_block = bytes([original_third_ciphertext_block[i-48] ^ change_for_fourth_block[i-48] for i in range(48, 50)])
new_ciphertext = new_ciphertext[:48] + modified_third_ciphertext_block + ciphertext[50:]

print(new_ciphertext.hex())

ciphertext=new_ciphertext
original_plaintext = b'u\x05\xa4\xbf\x19@\x9c\xe7[\xa7\x8b\xf8\xe1W\x1f\xb4\xe6@t\xf8\x8b\xcd`\xe3\x86\xc5\xd5j\x82F\xd57\x032\x1c)\xe1\xcf\x01\x18\x99\xecKvp\x92\xd1\xc2\x01\x01\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
original_second_ciphertext_block = ciphertext[32:48]
change_for_third_block = bytes([original_plaintext[i] ^ target_plaintext[i] for i in range(32, 48)])
modified_second_ciphertext_block = bytes([original_second_ciphertext_block[i-32] ^ change_for_third_block[i-32] for i in range(32, 48)])
new_ciphertext = ciphertext[:32] + modified_second_ciphertext_block + ciphertext[48:]
print(new_ciphertext.hex())

ciphertext=new_ciphertext
original_plaintext = b'u\x05\xa4\xbf\x19@\x9c\xe7[\xa7\x8b\xf8\xe1W\x1f\xb4\tN\xb3\xf7/&\xab\xd8\xde\x88/a\x99\xdf\x8eMAAA\xf0\x9f\xa4\xa3\xf0\x9f\xa4\xa3\xf0\x9f\xa4\xa3\x01\x01\x01\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
original_first_ciphertext_block = ciphertext[16:32]
change_for_second_block = bytes([original_plaintext[i] ^ target_plaintext[i] for i in range(16, 32)])
modified_first_ciphertext_block = bytes([original_first_ciphertext_block[i-16] ^ change_for_second_block[i-16] for i in range(16, 32)])
new_ciphertext = modified_iv + modified_first_ciphertext_block + ciphertext[32:]
print(new_ciphertext.hex())

ciphertext=new_ciphertext
original_plaintext = b'\xb7yV\xc9M\xc5\xb0_a\x8b\x91\x18jlt\x89em is HACKED BY AAA\xf0\x9f\xa4\xa3\xf0\x9f\xa4\xa3\xf0\x9f\xa4\xa3\x01\x01\x01\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
original_iv = ciphertext[:16]
change_for_first_block = bytes([original_plaintext[i] ^ target_plaintext[i] for i in range(16)])
modified_iv = bytes([original_iv[i] ^ change_for_first_block[i] for i in range(16)])
new_ciphertext=modified_iv+ciphertext[16:]
print(new_ciphertext.hex())

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def remove_last_block(ciphertext, block_size=16):
    # 确保密文长度至少是一个块的大小
    if len(ciphertext) < block_size:
        raise ValueError("Ciphertext is too short to remove a block.")
    
    # 计算新的密文长度
    new_length = len(ciphertext) - block_size
    
    # 切除最后一个块
    modified_ciphertext = ciphertext[:new_length]
    
    return modified_ciphertext

# 示例使用
hex_ciphertext = 'b0562d0383bb8b9b5666c5c10e35195c08a0df3ef8874868cffc21da643a3666682d91c4e64816577b2bd818f3db7968cbd74758bcace1a2521f153c29caada6ae999061ecf74e587a97073fd5c9e9b0'
ciphertext_bytes = hex_to_bytes(hex_ciphertext)  # 将十六进制字符串转换为字节
modified_ciphertext = remove_last_block(ciphertext_bytes)

print(modified_ciphertext.hex())  # 将结果转换回十六进制字符串以便查看