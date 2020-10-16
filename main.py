#Made By 5HR3D
#Github: https://github.com/5HR3D/
#Contact me: https://linktr.ee/5HR3D/
#Changing the author name in the code won't make you a programmer.


# importing
import os
import sys
import time
from moviepy.editor import *
from pytube import YouTube

# asking user for link
link = input("Enter YouTube video link :  ")
myvideo = YouTube(link)
#myvideo.get('mp4', '720p')

#print info
print("\nTitle :" + myvideo.title)

print("Duration :" + str(myvideo.length))

print("Views: " + str(myvideo.views))

print("Video ID: " + str(myvideo.video_id))

#des = input("Do you want the video description?(y/n): ")

'''if des == "y":
	print("\nDescription: " + myvideo.description)
elif des == "n":
	print("Okay.")
else:
	print("\ninvalid input!")'''
#Asking for description
while True:
	des = input("Do you want the video description?[y/n]: ")
	if des == "y":
		print("\nDescription: " + myvideo.description)
		break
	elif des == "n":
		print("Okay.")
		break
	else:
		print("invalid input!")


while True:
# showing user that the process has started
	op = input("\nProceed to Download?[y/n]: ")
	if op =="y":
		slowprint("[#]:> Downloding...")

# main code to download Video
		y = YouTube(link).streams.filter(progressive=True, file_extension='mp4')
		y.get_highest_resolution().download()

# showing user that the video has downloaded
		print("Video has been downloaded successfully :)")
		break

	elif op=="n":
		print("No Worries.")
		exit()
		break

	else:
		print("invalid input! Retry.")
		exit()
		break
#Convertion to mp3
while True:
	conv = input("\nDo you want to convert the downloaded (mp4)video to (mp3)audio?[y/n]: ")
	path = os.getcwd()
	if conv == "y":
		video = VideoFileClip(os.path.join((path) + "/" + myvideo.title + ".mp4"))
		video.audio.write_audiofile(os.path.join((path) + "/" + myvideo.title + ".mp3"))
		print("\nEnjoy! Thanks for using my script.")
		exit()
		break
	elif conv == "n":
		print("Enjoy! Thanks for using my script.")
		break
	else:
		print("invalid input! Retry.")
	


#ThankYou for using my script. Please follow me in Github and Star this Repo. 
