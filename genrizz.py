import os
for i in range(17):
    p = """cmd /c "ffmpeg -i rizz.mp4 -c:v libx264 -crf 20 -c:a aac -strict -2 -vf "subtitles=subs/"""+str(i)+""".srt:force_style='MarginV=100'" rizz/rizz"""+str(i)+""".mp4" """
    os.system(p)
