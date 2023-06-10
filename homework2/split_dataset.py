import os
import random
import shutil

# 创建保存图像的文件夹
def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

random.seed(1) # 随机种子

dataset_dir = os.path.join(".", "train")
train_dir = os.path.join(".", "train")
valid_dir = os.path.join(".", "valid")

train_pct = 0.8
valid_pct = 0.2

# print(dataset_dir)
for root, dirs, files in os.walk(dataset_dir):
    if root == './train':
        continue
    imgs = os.listdir(os.path.join(root))
    imgs = list(filter(lambda x: x.endswith('.jpg'), imgs))
    random.shuffle(imgs)
    img_count = len(imgs)
    train_point = int(img_count * train_pct)

    for i in range(img_count):
        if i < train_point:  # 保存0-train_point的图片到训练集
            continue
        out_dir = valid_dir +'/' + root[7:]
        makedir(out_dir) # 创建文件夹
        target_path = os.path.join(out_dir, imgs[i]) # 指定目标保存路径
        # print(target_path)
        src_path = os.path.join(root, imgs[i])  #指定目标原图像路径
        # print(src_path)
        shutil.move(src_path, target_path)  # 复制图片
