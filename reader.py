import json
import os

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "library.json")

if not os.path.exists(json_path):
    print("找不到 library.json")
    exit()

with open(json_path, "r", encoding="utf-8") as f:
    library = json.load(f)

print("我的图书馆里有这些宝贝：")
names = list(library.keys())
for i, name in enumerate(names):
    print(f"{i+1}. {name}")

while True:
    print("\n输入名字或编号（输入 exit 退出）：")
    user_input = input("> ").strip()

    if user_input.lower() == "exit":
        print("再见！")
        break

    # 判断输入的是编号还是名字
    if user_input.isdigit():
        idx = int(user_input) - 1
        if 0 <= idx < len(names):
            selected_name = names[idx]
        else:
            print("编号超出范围")
            continue
    else:
        selected_name = user_input

    # 查找并打开
    if selected_name in library:
        file_path = library[selected_name]["path"]
        print(f"正在打开：{selected_name}")
        print(f"路径：{file_path}")
        
        if os.path.exists(file_path):
            os.startfile(file_path)
        else:
            print(f"文件不存在，请检查路径：{file_path}")
    else:
        print(f"没找到《{selected_name}》")
    
    # 询问是否继续
    print("\n还要看别的吗？(y/n)")
    again = input("> ").strip().lower()
    if again != "y" and again != "yes":
        print("再见！")
        break