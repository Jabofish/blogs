import hashlib

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
    k = int(input("请输入数字k: "))  # 获取用户输入并转换为整数
    for s in range(k*1000000000, (k+1)*1000000000):
        result = process_string(str(s))  # 将数字转换为字符串
        if result:
            print(result)

if __name__ == "__main__":
    main()