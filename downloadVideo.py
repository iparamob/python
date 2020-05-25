# importing module https://github.com/ytdl-org/youtube-dl
import youtube_dl 

ydl_opts = {} 

def dwl_vid(): 
	with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
		ydl.download([zxt]) 

link_of_the_video = "https://www.youtube.com/watch?v=XXXXXX"
zxt = link_of_the_video.strip() 

dwl_vid() 
