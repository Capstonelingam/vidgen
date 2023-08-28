from moviepy.editor import *
import os
from natsort import natsorted



def stitch_video(output_folder):
    L = []
    for root, dirs, files in os.walk(f"{output_folder}"):


        #files.sort()
        files = natsorted(files)
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                filePath = os.path.join(root, file)
                video = VideoFileClip(filePath)
                L.append(video)

    final_clip = concatenate_videoclips(L)
    final_clip.to_videofile("../output/concat.mp4", fps=24, remove_temp=False)


if __name__ == "__main__":
    stitch_video("../output")
