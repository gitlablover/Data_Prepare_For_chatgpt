import re
import os
file_path = "E:\myCode\chatgpt\wechat\wechat_me\yhao\single\\txt\s001.txt"
def remove_newline(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()

    # 定义一个正则表达式，用于匹配不符合要求的换行符
    pattern = r'[^\}]\n'

    # 使用sub()方法替换不符合要求的换行符
    new_content = re.sub(pattern, '', content)

    # 将处理后的内容重新写入文件中
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(new_content)

if __name__ == '__main__':
    remove_newline(file_path)