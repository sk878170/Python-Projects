import moviepy
import moviepy.editor



# Import your video file
# Media file should be local
#You need to add an r before the file path as / in path is an escape character
video = moviepy.editor.VideoFileClip()
# Convert video to audio
audio = video.audio
audio.write_audiofile('new_audio2.mp3')


