import moviepy as mp
import numpy as np

def detect_silent_intervals(audio_clip, threshold=0.01, chunk_duration=0.05):
    """纯Python实现的静音检测，不依赖webrtcvad"""
    fps = audio_clip.fps
    chunk_size = int(fps * chunk_duration)
    audio_frames = audio_clip.to_soundarray()
    silent_intervals = []
    current_silent_start = None

    for i in range(0, len(audio_frames), chunk_size):
        chunk = audio_frames[i:i+chunk_size]
        rms = np.sqrt(np.mean(chunk**2))
        time = i / fps

        if rms < threshold:
            if current_silent_start is None:
                current_silent_start = time
        else:
            if current_silent_start is not None:
                silent_intervals.append((current_silent_start, time))
                current_silent_start = None
    return silent_intervals

def remove_silence(video_clip, threshold=0.01, min_silence_duration=0.3):
    audio = video_clip.audio
    silent_intervals = detect_silent_intervals(audio, threshold)

    keep_intervals = []
    prev_end = 0.0
    for s, e in silent_intervals:
        if e - s >= min_silence_duration:
            keep_intervals.append((prev_end, s))
            prev_end = e
    keep_intervals.append((prev_end, video_clip.duration))

    clips = [video_clip[s:e] for s, e in keep_intervals if e - s > 0.1]
    return mp.concatenate_videoclips(clips)

def auto_edit():
    print("开始处理视频...")

    # 1. 加载视频并截取5秒~50秒片段
    video = mp.VideoFileClip("test.mp4")
    video = video[5:50]

    # 2. 自动去掉静音片段
    print("正在去除静音...")
    final = remove_silence(video)

    # 3. 导出成品
    final.write_videofile("result.mp4")

    print("✅ 剪辑完成！已自动去掉静音片段")

if __name__ == "__main__":
    auto_edit()


