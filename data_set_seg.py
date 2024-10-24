import os
import random
import shutil

# 设置VOC数据集路径（图片和标签的文件夹）
voc_images_dir = '/home/ubuntu/gc(voc)/img'  # 图片的文件夹路径
voc_annotations_dir = '/home/ubuntu/gc(voc)/lable'  # 标签的文件夹路径

# 设置输出的训练集和验证集路径
train_images_dir = '/home/ubuntu/gc_modify/train/images'
train_annotations_dir = '/home/ubuntu/gc_modify/train/annotations'
val_images_dir = '/home/ubuntu/gc_modify/val/images'
val_annotations_dir = '/home/ubuntu/gc_modify/val/annotations'

# 创建输出文件夹，确保创建的是目录而不是文件
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_annotations_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_annotations_dir, exist_ok=True)

# 获取所有图片文件的文件名（不含扩展名）
image_files = [f.split('.')[0] for f in os.listdir(voc_images_dir) if f.endswith('.jpg')]

# 随机打乱图片文件列表
random.shuffle(image_files)

# 按7:3的比例划分为训练集和验证集
split_index = int(len(image_files) * 0.7)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

# 复制文件到训练集目录
for file in train_files:
    # 复制图片
    src_image_path = os.path.join(voc_images_dir, file + '.jpg')
    dest_image_path = os.path.join(train_images_dir, file + '.jpg')
    shutil.copyfile(src_image_path, dest_image_path)

    # 复制对应的标签（XML）
    src_annotation_path = os.path.join(voc_annotations_dir, file + '.xml')
    dest_annotation_path = os.path.join(train_annotations_dir, file + '.xml')
    shutil.copyfile(src_annotation_path, dest_annotation_path)

# 复制文件到验证集目录
for file in val_files:
    # 复制图片
    src_image_path = os.path.join(voc_images_dir, file + '.jpg')
    dest_image_path = os.path.join(val_images_dir, file + '.jpg')
    shutil.copyfile(src_image_path, dest_image_path)

    # 复制对应的标签（XML）
    src_annotation_path = os.path.join(voc_annotations_dir, file + '.xml')
    dest_annotation_path = os.path.join(val_annotations_dir, file + '.xml')
    shutil.copyfile(src_annotation_path, dest_annotation_path)

print("数据集划分完成，训练集和验证集已生成。")
