import os


# 读取 docs\post 文件夹下的所有文件夹名称

root_dir = "post"

array = [
    {"text": "JIULANG", "link": "/"},
]


def main():

    # 遍历根目录下的所有文件夹
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)

        # 检查是否为文件夹
        if os.path.isdir(folder_path):
            print(f"文件夹 A: {folder_path}")
            navItem = {
                "text": folder_name,
                "items": [],
            }
            items = []
            # 遍历文件夹 A 下的所有子文件夹
            for sub_folder_name in os.listdir(folder_path):
                sub_folder_path = os.path.join(folder_path, sub_folder_name)
                # 规范化路径
                # 将双反斜杠替换为单反斜杠
                sub_folder_path = sub_folder_path.replace("\\", "/")

                # 检查是否为文件夹
                if os.path.isdir(sub_folder_path):
                    print(f"子文件夹: {sub_folder_path}")
                    # 获取文件夹的下的文件的第一个文件
                    first_file = None
                    for file_name in os.listdir(sub_folder_path):
                        file_path = os.path.join(sub_folder_path, file_name)
                        if os.path.isfile(file_path):
                            first_file = file_name
                            break
                    items.append(
                        {
                            "text": sub_folder_name,
                            "link": sub_folder_path + "/" + first_file,
                        }
                    )
            navItem["items"] = items
            array.append(navItem)
    # 生成文件 navNew.mts 并且 export default 加 array数据
    with open(".vitepress/nav.mts", "w", encoding="utf-8") as f:
        f.write("export default ")
        f.write(str(array))


# main函数
if __name__ == "__main__":
    main()
