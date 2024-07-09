def getKeyLen(cipherText):
    keylength = 1
    maxCount = 0
    for step in range(1, 60):  # 循环密钥长度
        count = 0
        for i in range(step, len(cipherText) - step):
            if cipherText[i] == cipherText[i + step]:
                count += 1
        if count > maxCount:
            maxCount = count
            keylength = step
        print(step, count)
    return keylength

def create_matrix(cipherText, keyLength):
    matrix = []
    for i in range(0, len(cipherText), keyLength):
        row = list(cipherText[i:i + keyLength])
        matrix.append(row)
    return matrix

with open('cipher.txt', 'r') as file:
    cipherText = file.read()

keyLength = getKeyLen(cipherText)
matrix = create_matrix(cipherText, keyLength)
print(keyLength)
# 将矩阵按行写入文件
with open('cipher_processed.txt', 'w') as outfile:
    for row in matrix:
        outfile.write(repr('    '.join(row)) + '\n')