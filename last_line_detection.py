import os

folder_path = "E:\myCode\chatgpt\wechat\wechat_me\yhao\single\\txt"
if __name__ == '__main__':

    for file_name in os.listdir(folder_path):
        new_lines = []
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r+", encoding="utf-8") as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    if "completion" in lines[i]:
                        new_lines.append(lines[i])
                file.close()
            with open(file_path, "w", encoding="utf-8") as file:
                file.write((''.join(new_lines)))
                file.close()
