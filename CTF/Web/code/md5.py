import hashlib
import itertools
import string

def check_md5_conditions(s):
    md5_hash = hashlib.md5(s.encode()).hexdigest()
    if md5_hash.startswith('0e') and md5_hash[2:].isdigit():
        return f"以0e开头的字符串: {s} -> {md5_hash}"
    if md5_hash.startswith("'or"):
        return f"以'or开头的字符串: {s} -> {md5_hash}"
    return None

def process_string(s):
    random_string = ''.join(s)
    result = check_md5_conditions(random_string)
    if result:
        return result
    return None

def main():
    characters = string.digits
    for length in range(1, 21):
        # 创建一个字符串生成器
        strings = itertools.product(characters, repeat=length)
        # 顺序处理字符串
        for s in strings:
            result = process_string(s)
            if result:
                print(result)
        print(f"完成长度为{length}的字符串遍历。")

if __name__ == "__main__":
    main()