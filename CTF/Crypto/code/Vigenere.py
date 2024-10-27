def getKeyLen(cipherText):
    keylength = 1
    maxCount = 0
    for step in range(1, 30):  # 循环密钥长度
        count = 0
        for i in range(step, len(cipherText) - step):
            if cipherText[i] == cipherText[i + step]:
                count += 1
        #print(step, count)
        if count > maxCount:
            maxCount = count
            keylength = step
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
        
def traverse_columns(matrix):
    """
    按列遍历矩阵并返回列的列表
    """
    columns = []
    for col_index in range(len(matrix[0])):
        column = [row[col_index] for row in matrix if col_index < len(row)]
        columns.append(column)
    return columns

columns = traverse_columns(matrix)

'''
def encrypt(s,k):
    out=''
    for i in range(len(s)):
        index=text_list.index(s[i])
        index*=k[i%len(k)]
        index%=97
        out+=text_list[index]
    return out
'''
#根据加密逻辑对每一列进行破解，对每一列遍历每一个可能的key值，统计将该列解密后的结果的字母总数，字母总数最多的key值即为该列的key值
def crack_column(column):
    text_list = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
    max_count = 0
    key = 0
    for i in range(1, 97):
        count = 0
        for c in column:
            index = text_list.index(c)
            index *= i
            index %= 97
            count += index
        if count > max_count:
            max_count = count
            key = i
    return key

#对每一列进行破解
keys = [crack_column(column) for column in columns]
print(keys)

#根据key值解密密文
def decrypt(cipherText, keys):
    text_list = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
    plainText = ''
    for i in range(len(cipherText)):
        index = text_list.index(cipherText[i])
        index *= keys[i % len(keys)]
        index %= 97
        plainText += text_list[index]
    return plainText

plainText = decrypt(cipherText, keys)
print(plainText)