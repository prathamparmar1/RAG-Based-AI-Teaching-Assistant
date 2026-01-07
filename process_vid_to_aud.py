# Converts videos to mp3
import os
import subprocess

files = os.listdir("videos")

for file in files:
    # print(file)
    tutorial_number = file.split("Tutorial_")[1].split("_")[0]
    # print(tutorial_number)
    file_name = file.split("_Sigma")[0]
    # print(tutorial_number,  file_name)
    subprocess.run(['ffmpeg', '-i', f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])

# files = os.listdir("audios")

# for file in files:
#     subprocess.run([ 'ffmpeg', '-ss', '0', '-i', f'audios/{file}', '-t', '10', '-c', 'copy', f'audio_cut/{file}.mp3'])
#     # print(file)