import pandas as pd
import json
import csv
if __name__ == '__main__':


    # 从文件中加载JSON数据
    with open('s0040.json', 'r', encoding="utf-8") as f:
        data = json.load(f)

    # 将JSON数据写入CSV文件中


    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())  # 写入CSV文件头
        for item in data:
            writer.writerow(item.values())  # 写入CSV行数据
