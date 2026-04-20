import moviepy as mp

def auto_edit():
    print("开始处理视频...")

    # 读取视频
    video = mp.VideoFileClip("test.mp4")

    # 截取：45秒 ~ 60秒
    final = video[45:60]

    # 导出视频
    final.write_videofile("result.mp4")

    print("导出完成：result.mp4")

if __name__ == "__main__":
    auto_edit()
