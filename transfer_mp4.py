import os
from moviepy.editor import VideoFileClip

def convert_video(input_path, output_path):
    try:
        # 使用 MoviePy 加载视频并写入新的编码
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Converted: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error occurred while converting {input_path}: {e}")

def batch_convert_videos(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.mp4'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.mp4")
            convert_video(input_path, output_path)

    print("Batch conversion completed!")

# 输入和输出文件夹
input_folder = r"D:\ALL_files\publications\rvt2_\rebuttal\video-1"
output_folder = r"D:\ALL_files\publications\rvt2_\rebuttal\video-1/convert"

batch_convert_videos(input_folder, output_folder)
