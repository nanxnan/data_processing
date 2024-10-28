import json

# 旧标签到新标签的映射
label_mapping = {
    "1_chongkong": "punching_hole",
    "2_hanfeng": "welding_line",
    "3_yueyawan": "crescent_gap",
    "4_shuiban": "water_spot",
    "5_youban": "oil_spot",
    "6_siban": "silk_spot",
    "7_yiwu": "inclusion",
    "8_yahen": "rolled_pit",
    "9_zhehen": "crease",
    "10_yaozhe": "waist_folding"
}

# 输入和输出的文件路径
input_file = '/home/ubuntu/gc_modify/annotations/instances_val.json'  # 原始标签文件路径
output_file = '/home/ubuntu/gc_modify/annotations/instances_val.json_english.json'  # 输出的新标签文件路径

# 读取 JSON 文件
with open(input_file, 'r') as f:
    data = json.load(f)

# 替换类别名称
for category in data['categories']:
    old_name = category['name']
    if old_name in label_mapping:
        category['name'] = label_mapping[old_name]

# 写入转换后的 JSON 文件
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print("标签名称转换完成，结果已保存到", output_file)
