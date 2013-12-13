import os
import subprocess
import random
import argparse

## Add the following to the powershell profile
# function play($show, $count)
# {
# 	python C:\directory\play.py $show $count
# }

futurama_path = 'D:\\video\\Futurama (complete)\\'
tng_path = 'D:\\trek\\The Next Generation\\'
vlc_path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"

parser = argparse.ArgumentParser()

parser.add_argument("show", help=" The show you want to play. 'tng' or 'futu' ")
parser.add_argument("play_count", type=int, help="number of episodes you want to play")

args = parser.parse_args()

if args.show.lower() == 'tng':
	show_path = tng_path
elif args.show.lower() == 'futu':
	show_path = futurama_path
else:
	print "pick either tng or futurama"

episodes = []

def play_episode(video):
	subprocess.call([vlc_path, video, '--play-and-exit', '--fullscreen'])

for i in range(args.play_count):
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

