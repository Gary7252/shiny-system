# 修复：新版 moviepy 正确导入方式（无 editor）
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

# 自动剪辑（最简单、最稳定、不报错版本）
def auto_edit():
    print("开始读取视频...")
    
    # 读取你的视频 test.mp4
    clip = VideoFileClip("test.mp4")

    # 直接导出到当前文件夹，不报错
    clip.write_videofile(
        "result.mp4",
        codec="libx264",
        audio_codec="aac"
    )

    print("✅ 剪辑完成！")
    print("视频已保存到当前文件夹：result.mp4")

if __name__ == "__main__":
    auto_edit()