import os
import json
from pathlib import Path

def scan_files_to_json(folder_path, output_json="library.json"):
    """
    扫描指定文件夹下的所有 .mp4 和 .pdf 文件，
    生成 JSON 格式：{文件名（不含扩展名）: {path: 完整路径, tags: [], last_opened: null}}
    
    参数:
        folder_path: 要扫描的文件夹路径
        output_json: 输出的 JSON 文件名（默认为 output.json）
    """
    # 支持的扩展名
    extensions = {'.mp4', '.pdf'}
    
    # 存储结果
    result = {}
    
    # 将输入路径转换为 Path 对象
    root_dir = Path(folder_path)
    
    # 检查文件夹是否存在
    if not root_dir.exists():
        print(f"错误：文件夹 '{folder_path}' 不存在")
        return
    if not root_dir.is_dir():
        print(f"错误：'{folder_path}' 不是一个文件夹")
        return
    
    # 递归遍历文件夹
    for file_path in root_dir.rglob("*"):
        # 检查是否为文件且扩展名在支持的列表中
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            # 获取文件名（不含扩展名）
            stem = file_path.stem
            # 获取完整路径（绝对路径）
            full_path = str(file_path.absolute())
            
            # 添加到结果字典
            result[stem] = {
                "path": full_path,
                "tags": [],
                "last_opened": None
            }
    
        # 将结果写入 JSON 文件（强制写到脚本所在目录）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_json)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"扫描完成！共找到 {len(result)} 个文件。")
    print(f"结果已保存至: {output_path}")

if __name__ == "__main__":
    # 使用示例：请将下面的路径替换为您要扫描的文件夹路径
    # folder_to_scan = input("请输入要扫描的文件夹路径: ").strip()
    # 或者直接指定路径：
    folder_to_scan = "C:/Users/lenovo/Desktop/MyLibrary/media_files"
    
    scan_files_to_json(folder_to_scan, output_json="library.json")