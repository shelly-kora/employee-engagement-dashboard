import pandas as pd
import os

# Input and output paths
input_file = "/Users/hongleilu/Desktop/2024年员工敬满度调研/【文字分析使用-建议】心动 2024 年度员工满意度调研_1093.xlsx"
output_folder = "/Users/hongleilu/Desktop/2024年员工敬满度调研"
output_file = os.path.join(output_folder, "【已分类-IT相关】心动 2024 年度员工满意度调研_1093.xlsx")

# Read the Excel file
print("Reading Excel file...")
df = pd.read_excel(input_file)

# Check if column D exists
if len(df.columns) < 4:
    print("Error: The Excel file doesn't have at least 4 columns")
    exit(1)

# Get the actual column name for column D (index 3)
column_d_name = df.columns[3]
print(f"Column D name: {column_d_name}")

# Create column E if it doesn't exist
if len(df.columns) < 5:
    column_e_name = "分类"
    df[column_e_name] = ""
else:
    column_e_name = df.columns[4]

# Keywords related to IT, hardware, software, and network
it_keywords = [
    "IT", "电脑", "笔记本", "硬件", "软件", "系统", "网络", "网速", 
    "服务器", "VPN", "设备", "设施", "信息技术", "信息安全", "网络安全",
    "技术支持", "技术问题", "网络问题", "技术部门", "电子设备", "配置",
    "升级", "更新", "安装", "维修", "维护", "故障", "网页", "应用",
    "App", "数据", "数据库", "存储", "云服务", "办公软件", "办公设备",
    "打印机", "路由器", "无线", "WiFi", "宽带", "网线", "连接", "程序",
    "崩溃", "卡顿", "延迟", "内网", "外网", "电源", "显示器", "键盘",
    "鼠标", "耳机", "摄像头", "麦克风", "充电器", "接口", "智能手机"
]

# Categorize entries in column D
print("Categorizing entries...")
categorized_count = 0
for idx, row in df.iterrows():
    if pd.notna(row[column_d_name]):
        content = str(row[column_d_name]).lower()
        if any(keyword.lower() in content for keyword in it_keywords):
            df.at[idx, column_e_name] = "IT相关"
            categorized_count += 1

# Save the modified file
print(f"Saving results to {output_file}...")
df.to_excel(output_file, index=False)

print(f"Categorization complete. {categorized_count} entries marked as 'IT相关'.") 