from mutagen.mp3 import MP3

audio = MP3('./songs/128-Mann Jogiya - Arijit Singh 128 Kbps (1).mp3')
duration = audio.info.length
print(duration)

