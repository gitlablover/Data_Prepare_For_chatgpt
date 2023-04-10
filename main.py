import glob

from bs4 import BeautifulSoup
from lxml import html
import os

#潘婧#张欣萌#陈文涛#黄欣#周齐凯#王博天#3人群#妈
# 读取HTML文件
def operation1(file):
    with open(file, 'r', encoding='utf-8') as f:
        html_file = f.read()

    # 使用BeautifulSoup解析HTML
    parser = html.HTMLParser(remove_blank_text=True)
    soup = BeautifulSoup(html_file, 'lxml', parser=parser)

    # 找到聊天记录的开图
    msgs_start = soup.find('div', {'class': 'msgs'})
    if msgs_start:
        # 找到所有消息
        msgs_all = msgs_start.find_all('span', {'class': 'dont-break-out msg-text'})
        if msgs_all:
            # 一段对话由大括号开始
            conversations = ""
            last_is_left = bool(0)
            for msg in msgs_all:
                parent = msg.parent.parent.get('class', [])
                print(msg)
                print("left" in parent)
                # 假如是问题，且之前不是问题。
                if ("left" in parent) and not last_is_left:
                    # 新的问题
                    text = "<EOS>\"} {\"prompt\": " + "\"" + msg.text.strip()
                    last_is_left = bool(1)
                    conversations = conversations + text
                elif "left" in parent:
                    # 还是问题的延续
                    text = "," + msg.text.strip()
                    last_is_left = bool(1)
                    conversations = conversations + text
                # 假如是问题结束了，回答的开始
                elif "right" in parent and last_is_left:
                    text = "\", \"completion\": \"" + msg.text.strip()
                    last_is_left = bool(0)
                    conversations = conversations + text
                # 假如是回答的继续
                elif "right" in parent:
                    text = "," + msg.text.strip()
                    last_is_left = bool(0)
                    conversations = conversations + text
            conversations = conversations + "<EOS>\""
            return conversations
        # 将聊天记录保存到文本文件中


folder_path = "E:\myCode\chatgpt\wechat\wechat me\yhao\single\\txt"
html_files = glob.glob(os.path.join(folder_path, "*.txt"))
for filename in html_files:
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write('}')
        f.close
#with open("E:\myCode\chatgpt\wechat\wechat me\袁hao\single\extra\唐一杰、陈俊毅.txt",'w',encoding='utf-8') as f:
 #   f.write(operation1("E:\myCode\chatgpt\wechat\wechat me\袁hao\single\extra\\3q.html"))
  #  f.close()
'''
for filename in html_files:
    file_path = os.path.join(folder_path, filename)
    with open(file_path + ' conversations.txt', 'a', encoding='utf-8') as f:
        if operation1(file_path):
            f.write(operation1(file_path))
        f.close()
'''