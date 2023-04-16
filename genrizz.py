import os
directory = os.getcwd()
dir_path = directory+'\subs'
rizz = directory+'\\rizz'
os.mkdir(rizz)

count = 0
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
for i in range(count):
    p = """cmd /c "ffmpeg -i rizz.mp4 -c:v libx264 -crf 20 -c:a aac -strict -2 -vf "subtitles=subs/"""+str(i)+""".srt:force_style='MarginV=100'" rizz/rizz"""+str(i)+""".mp4" """
    os.system(p)
