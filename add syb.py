import os

folder_path = "E:\myCode\chatgpt\wechat\wechat_me\yhao\single\\txt"
if __name__ == '__main__':

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            # Read in the original file
            with open(os.path.join(folder_path, filename), "r", encoding='utf-8') as f:
                lines = f.readlines()

            # Find the first line with "{"
            for i, line in enumerate(lines):
                if "{" in line:
                    break

            # Write out the modified file
            with open(os.path.join(folder_path, filename), "w", encoding='utf-8') as f:
                f.writelines(lines[i:])