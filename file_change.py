import glob
import os
if __name__ == '__main__':

# 打开文件
    with open('E:\myCode\chatgpt\wechat\wechat_me\yhao\single\\txt\s0041.json', 'r+', encoding="utf-8") as file:
        # 读取文件中的所有内容
        content = file.read()

        # 使用 replace() 方法将 "}{ " 替换为 "}{\n"
        updated_content = content.replace('}{', '}\n{')

        # 将替换后的文本写回原文件中
        file.seek(0)
        file.write(updated_content)
        file.truncate()
