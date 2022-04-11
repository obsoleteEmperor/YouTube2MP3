from pytube import YouTube
from pytube import Playlist
import os 

#destination to save file
#eg 'D:\\Music'
destination = '#put destination path here'
count_m = 0
#The playlist to download from
#Make sure the playlist is public or unlisted. Else we can't read or view the playlist
p = Playlist('#paste the playlist url here')
for video in p.videos:
	# extract only audio
	video_audio_only = video.streams.get_audio_only()            
	'''(code to get best quality is used. The code below can also be used, 
	but not sure what quality audio comes, but the size of the audio file is small.)   
	video.streams.filter(only_audio=True).first()'''

	# download the file
	try:
		out_file = video_audio_only.download(output_path=destination)

		# save the file
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)

		# result of success
		print(video.title + " has been successfully downloaded.")
		count_m +=1
	except:
		continue 

print(count_m)


#find out why some are getting timedout



