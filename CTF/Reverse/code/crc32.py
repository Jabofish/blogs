# coding:utf-8

"""
Author：spaceman
"""

import binascii
import string 
from time import sleep

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

# 进度条
def progress(percent=0, width=40):
    left = width * percent // 95
    right = width - left
    print ('\r[', '#' * left, ' ' * right, ']',f' {percent:.0f}%',sep='', end='', flush=True)

# 一位字节
def crc1(strs,dic):
    strs = hex(int(strs,16))
    rs = ''
    for i in dic:
        s = i
        if hex(binascii.crc32(s.encode())) == strs:
            rs += s
            print (strs+'  ： '+s)
    return rs

# 两位字节
def crc2(strs,dic):
    strs = hex(int(strs,16))
    rs = ''
    for i in dic:
        for j in dic:
            s = i + j
            if hex(binascii.crc32(s.encode())) == strs:
                rs += s
                print (strs+'  ： '+s)
    return rs

# 三位字节
def crc3(strs,dic):
    strs = hex(int(strs,16))
    rs = ''
    for i in dic:
        for j in dic:
            for k in dic:
                s = i+j+k
                if hex(binascii.crc32(s.encode())) == strs:
                    rs += s
                    print (strs+'  ： '+s)
    return rs

# 四位字节
def crc4(strs,dic):
    strs = hex(int(strs,16))
    rs = ''
    it = 1
    for i in dic:
        for j in dic:
            for k in dic:
                for m in dic:
                    s = i+j+k+m
                    if hex(binascii.crc32(s.encode())) == strs:
                        rs += s
                        print ()
                        print (strs+'  ： '+s)
                        print ('\n')
        progress(it)
        sleep(0.1)
        it += 1
    return rs
    

# 五位字节
def crc5(strs,dic):
    strs = hex(int(strs,16))
    rs = ''
    it = 1
    for i in dic:
        progress(it)
        for j in dic:
            for k in dic:
                for m in dic:
                    for n in dic:
                        s = i+j+k+m+n
                        if hex(binascii.crc32(s.encode())) == strs:
                            rs += s
                            print ()
                            print (strs+'  ： '+s)
                            print ('\n')
        sleep(0.1)
        it += 1
    return rs

# 计算碰撞 crc 
def CrackCrc(crclist,length):
    print ()
    print ("正在计算...")
    print ()
    dic = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~''' # 碰撞需要的字符字典
    dic = dic[::-1]
    text = ''
    for i in crclist:
        if length == '1':
            text += crc1(i,dic)
        if length == '2':
            text += crc2(i,dic)
        if length == '3':
            text += crc3(i,dic)
        if length == '4':
            text += crc4(i,dic)
        if length == '5':
            text += crc5(i,dic)
    print ('\n')
    if text == '':
        print ("碰撞失败,无结果")
        exit()
    print ("字符顺序组合：",end=' ')
    print ()
    print (text)
    print ()
    input("回车确认结束程序...")

# 主函数
print ('''
##############################

###### Author：spaceman ######

### Thank you for your use ###

##############################
''')
listcrc = [] # 用于存储crc值
length = (input("请输入文本字节大小(1-5)：")) # 即文本内容大小，如文本内容为flag，大小即为4
if is_number(length) == False or length not in ("1,2,3,4,5"):
    exit("非指定数字，退出")
print ()
while 1:
    crc = input('请输入crc值(例如:d1f4eb9a,输入n完成输入):')
    if crc == 'n':
        break
    crc = '0x'+crc
    if len(crc) != 10:
        print ("rcr长度不对,请重新输入")
        continue
    listcrc.append(crc)

CrackCrc(listcrc,length)
