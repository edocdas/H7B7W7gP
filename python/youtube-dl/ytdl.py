import yt_dlp as yt

# help(yt.YoutubeDL)

ydl_opts = {"merge_output_format":"webm", "listformats":False, "format":"bestvideo+bestaudio/best", "outtmpl":"C:\\Users\\Ken\\Documents\\Git\\python-program-master\\\
youtube-dl\\download_vid\\%(extractor)s\\%(title)s [%(resolution)s][%(fps)s fps]"}

file = open("C:\\Users\\Ken\\Documents\\Git\\python-program-master\\youtube-dl\\input.txt", "r")

list_url = []
print("Please input url to download.")
input_url = file.readline()
while input_url != "#":
    list_url.append(input_url)
    input_url = file.readline()

with yt.YoutubeDL(ydl_opts) as ydl:
    ydl.download(list_url)
