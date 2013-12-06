import os
import subprocess
import random
from sys import argv

if len(argv) < 2:
	episodes_to_play = 1
else:
	episodes_to_play = int(argv[1])

futurama_path = 'D:\\video\\Futurama (complete)\\'
vlc_path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
episodes = []

def play_episode(video):
	subprocess.call([vlc_path, video, '--play-and-exit', '--fullscreen'])

show_path = futurama_path

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

