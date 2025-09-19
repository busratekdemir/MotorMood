import subprocess

url = "https://www.youtube.com/watch?v=4jt9Ival5vI"
output = "motor7.mp3"

# sadece ses indir (mp3 formatında)
subprocess.run([
    "yt-dlp", "-x", "--audio-format", "mp3", "-o", output, url
])
