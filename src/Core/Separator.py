import moviepy.editor as me
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else :
        os.system("clear")

clear()

file_dir_input = str(input("Enter your relative file directory "))
output_name = str(input("Enter your output name "))
output_name += ".mp3"

video = me.VideoFileClip(file_dir_input)
video.audio.write_audiofile(output_name) 