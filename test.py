from moviepy.editor import VideoFileClip

video_path = r"C:\Users\andth\Downloads\audio to text\test.mp4"
audio_path = "output_audio.wav"

video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_path)
