import os
import uuid
from datetime import datetime

# 定义图片的扩展名
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.mov')

# 设置相对路径，假设文件夹名为 "images"
folder_path = "./"

# 获取文件夹中的文件
files = os.listdir(folder_path)

# 第一步：将所有文件重命名为唯一的临时名称
for file_name in files:
    if file_name.lower().endswith(image_extensions):  # 只处理图片文件
        file_path = os.path.join(folder_path, file_name)
        
        # 生成唯一的临时文件名，使用 UUID 确保唯一性
        unique_name = str(uuid.uuid4()) + os.path.splitext(file_name)[1]  # 保留文件扩展名
        unique_file_path = os.path.join(folder_path, unique_name)
        
        # 重命名文件为唯一文件名
        os.rename(file_path, unique_file_path)
        print(f"temp rename: {file_name} -> {unique_name}")

# 第二步：按格式要求并按创建时间顺序重命名
# 获取文件夹中的文件（已经是唯一的文件名）
files = os.listdir(folder_path)

# 获取用户输入的起始编号
try:
    start_number = int(input("please input start number: "))
except ValueError:
    print("input error, use default 1")
    start_number = 1

# 筛选出所有图片文件并附带创建时间
image_files_with_ctime = [
    (file_name, os.path.getctime(os.path.join(folder_path, file_name)))
    for file_name in files
    if file_name.lower().endswith(image_extensions)
]

# 按照创建时间排序
image_files_with_ctime.sort(key=lambda x: x[1])

# 计数器（从用户输入的数字开始）
counter = start_number

# 遍历排序后的文件，按格式要求重命名
for file_name, _ in image_files_with_ctime:
    file_path = os.path.join(folder_path, file_name)
    
    # 获取文件的修改日期
    file_time = os.path.getmtime(file_path)  # 获取修改时间（秒）
    formatted_time = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d')  # 格式化时间
    
    
    
    # 设置新的文件名: WF-YYYY-MM-DD(PXX)
    file_extension = os.path.splitext(file_name)[1]  # 获取文件的后缀名
    new_file_name = f"WF-{formatted_time}_(P{counter:02d}){file_extension}"
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # 重命名文件
    os.rename(file_path, new_file_path)
    print(f"final rename: {file_name} -> {new_file_name}")
    
    # 计数器加1
    counter += 1

print("all done!")

