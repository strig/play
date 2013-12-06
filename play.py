import os
import subprocess
import random
from sys import argv


futurama_path = 'D:\\video\\Futurama (complete)\\'
tng_path = 'D:\\trek\\The Next Generation\\'
vlc_path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"


if len(argv) < 2:
	episodes_to_play = 1
	show_path = futurama_path
elif len(argv) < 3:
	episodes_to_play = 1
	if str(argv[1]).lower() == 'tng':
		show_path = tng_path
	else:
		show_path = futurama_path
else:
	if str(argv[1]).lower() == 'tng':
		show_path = tng_path
	else:
		show_path = futurama_path
	episodes_to_play = int(argv[2])


episodes = []

def play_episode(video):
	subprocess.call([vlc_path, video, '--play-and-exit', '--fullscreen'])

for i in range(episodes_to_play):
	# randomly select a list of episodes to play
	season =  random.choice(os.listdir(show_path))
	while season == "Futurama Movies":
		season =  random.choice(os.listdir(show_path))
	season_path = show_path + season + "\\"
	episode = random.choice(os.listdir(season_path))
	while episode == 'Thumbs.db':
		episode = random.choice(os.listdir(season_path))
	episode_path = season_path + episode
	episodes.append(episode_path)

for ep in episodes:
	print ep
	play_episode(ep)

