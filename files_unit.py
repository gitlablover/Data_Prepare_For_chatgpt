import glob
import os
folder_path = "E:\myCode\chatgpt\wechat\wechat_me\yhao\single\\txt"
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
new_file_path = "E:\myCode\chatgpt\wechat\wechat_me\yhao\single\\txt\s001.txt"

if __name__ == '__main__':

    with open(new_file_path, 'w', encoding="utf-8") as f:
        for file_path in txt_files:
            with open(file_path, 'r', encoding="utf-8") as txt_file:
                f.write(txt_file.read())
            print(file_path + " done")
            f.write('\n')
    f.close()