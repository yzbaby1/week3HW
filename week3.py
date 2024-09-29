import csv
import json

# 打開 CSV 檔案並讀取
with open('input.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]

# 將數據寫入 JSON 檔案
with open('output.json', mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)