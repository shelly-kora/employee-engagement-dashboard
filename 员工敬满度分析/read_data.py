#!/usr/bin/env python3
import pandas as pd
import json

# 读取Excel文件
xl = pd.ExcelFile('定稿初始数据.xlsx')
data = {}

print('工作表名称:', xl.sheet_names)

for sheet in xl.sheet_names:
    print(f'\n=== {sheet} ===')
    df = pd.read_excel(xl, sheet_name=sheet)
    print('列名:', df.columns.tolist())
    print('行数:', len(df))
    print('数据:')
    print(df)
    
    # 将数据保存到字典中
    data[sheet] = df.to_dict('records')

# 保存为JSON文件
with open('survey_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    
print('\n数据已保存到 survey_data.json') 