# shiny-system
Python 视频自动剪辑脚本，基于新版 moviepy 规范编写

## 项目说明
本项目从需求到调试完整记录了开发过程，
解决了Python 多版本冲突、旧版 moviepy 语法废弃等问题，
最终统一环境并实现可稳定运行的视频剪辑功能。

## 运行环境
- Python 3.13.13（安装在 D 盘，统一环境不混用）
- Windows 系统
- 新版 moviepy（不使用废弃的 editor / subclip）

## 安装依赖
```bash
python -m pip install moviepy

使用方法
将视频重命名为 test.mp4 放在项目目录
运行脚本
bash
运行
python video_test.py
生成结果视频 result.mp4

规范说明
统一使用 D 盘 Python 环境，不混用多版本
安装库使用 python -m pip install
新版 moviepy 导入：import moviepy as mp
剪辑使用切片语法，不使用 subclip
输出文件直接保存在当前目录
