flag = "A{1*41Q^n&AsHacmTg11AlpB!Z3TL}"
FT = [[0 for _ in range(10)] for _ in range(3)]
for i in range(3):
    for j in range(10):
        index = i*10 + j
        if index < len(flag):
            FT[i][j] = ord(flag[index])
# 打印矩阵
for row in FT:
    print(row)
RT=FT
result = b''
for i in range(10):
	for j in range(3):
		result += bytes([RT[j][i]])
print(result)