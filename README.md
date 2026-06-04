# MyLibrary

一个用 Python 写的本地媒体文件管理工具。

## 功能
- 自动扫描文件夹中的视频文件
- 生成文件目录
- 输入名字即可播放视频

## 使用方法
1. 将视频文件放入 `media_files` 文件夹
2. 运行 `scan.py` 扫描文件
3. 运行 `reader.py`，输入编号或名称播放

## 文件说明
- `scan.py`：扫描文件夹，生成 library.json
- `reader.py`：读取 library.json，提供播放界面
