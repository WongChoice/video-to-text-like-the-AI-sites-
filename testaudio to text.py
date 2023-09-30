from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import speech_recognition as sr

# Function to create dynamic text clips
def dynamic_text_clips(text, duration, fontsize=24, color='white', max_words=5):
    clips = []
    words = text.split()
    current_time = 0.0
    word_index = 0

    while word_index < len(words):
        # Extract the next set of words (up to max_words)
        current_words = words[word_index:word_index + max_words]
        current_text = ' '.join(current_words)
        word_index += max_words

        text_clip = TextClip(current_text, fontsize=fontsize, color=color)
        text_clip = text_clip.set_duration(duration)
        clips.append(text_clip.set_start(current_time))
        current_time += duration

    return clips

# Step 1: Video to Audio Conversion
video_path = "input_video.mp4"
audio_path = "output_audio.wav"

video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_path)

# Step 2: Audio to Text Conversion
audio_path = "output_audio.wav"

recognizer = sr.Recognizer()

with sr.AudioFile(audio_path) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)

print("Recognized Text:", text)

# Step 3: Text Overlay onto Video with Dynamic Highlighting
output_path = "output_video.mp4"

# Get the duration of the original video
video_duration = video_clip.duration

# Create dynamic text clips (5 words at a time)
text_clips = dynamic_text_clips(text, duration=2.0, fontsize=24, color='white', max_words=5)

# Overlay the dynamic text clips onto the original video at the bottom center
position = ('center', 'bottom')
text_clips = [clip.set_position(position) for clip in text_clips]

# Composite the video with text overlay
video_with_text = CompositeVideoClip([video_clip.set_duration(video_duration)] + text_clips)

# Write the final video with dynamic text overlay
video_with_text.write_videofile(output_path, codec='libx264')
