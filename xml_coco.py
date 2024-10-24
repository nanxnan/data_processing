import os
import json
import xml.etree.ElementTree as ET

class Converter:
    @staticmethod
    def voc2coco(xmlpath):
        categories = []
        coco_dataset = {
            'licenses': [],
            'images': [],
            'annotations': [],
            'info': {},
            'categories': categories,
        }

        # 获取文件夹中的所有 XML 文件
        xmlList = os.listdir(xmlpath)
        for xmlname in xmlList:
            if xmlname.endswith(".xml"):
                xml_file = os.path.join(xmlpath, xmlname)
                tree = ET.parse(xml_file)
                root = tree.getroot()

                # 提取图像尺寸信息
                size = root.find('size')
                file_name = root.find("filename").text

                # 图像信息
                image_info = {
                    "id": len(coco_dataset['images']) + 1,
                    "file_name": file_name,
                    "width": int(size.find('width').text),
                    "height": int(size.find('height').text),
                    "date_captured": "",
                    "license": None,
                    "coco_url": "",
                    "flickr_url": ""
                }
                coco_dataset['images'].append(image_info)

                # 解析每个物体的标注信息
                for obj in root.findall('object'):
                    name = obj.find('name').text

                    # 处理类别信息
                    clist = [c['name'] for c in categories]
                    if name not in clist:
                        category_id = len(categories) + 1
                        categories.append({
                            'id': category_id,
                            'name': name,
                            'supercategory': 'object'
                        })
                    else:
                        for c in categories:
                            if c['name'] == name:
                                category_id = c['id']

                    # 提取边界框信息
                    bnd_box = obj.find('bndbox')
                    bbox = [
                        int(bnd_box.find('xmin').text),
                        int(bnd_box.find('ymin').text),
                        int(bnd_box.find('xmax').text),
                        int(bnd_box.find('ymax').text)
                    ]
                    bbox = [
                        bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]
                    ]

                    # 标注信息
                    ann_info = {
                        'id': len(coco_dataset['annotations']) + 1,
                        'image_id': len(coco_dataset['images']),
                        'category_id': category_id,
                        'bbox': bbox,
                        'area': bbox[2] * bbox[3],
                        'iscrowd': 0
                    }
                    coco_dataset['annotations'].append(ann_info)

        return coco_dataset

# 指定包含多个 XML 文件的文件夹路径
xml_folder = '/home/ubuntu/gc_modify/val/lable'  # 将此路径替换为实际 XML 文件夹路径

# 调用转换方法并获取 COCO 格式数据
coco_data = Converter.voc2coco(xml_folder)

# 保存为 JSON 文件
output_json_path = '/home/ubuntu/gc_modify/val/annotations.json'  # 设置保存 JSON 文件的路径
with open(output_json_path, 'w') as json_file:
    json.dump(coco_data, json_file, indent=4)

print("XML 文件夹已成功转换为 COCO 格式的 JSON 文件。")
