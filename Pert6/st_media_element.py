import streamlit as st
from PIL import Image

image = Image.open("sunrise.jpg")

st.image(image, caption='Sunrise by the mountains')
st.write("THE SUNRISE GOES ON")
st.write("Image Link: https://www.freepik.com/free-photos-vectors/sunrise ")


import streamlit as st
import numpy as np

audio_file = open('muriel.ogg', 'rb')
audio_bytes = audio_file.read()


st.audio(audio_bytes, format='audio/ogg')
st.write("Audio Link: https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg ")


sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)



import streamlit as st

video_file = open('aurora.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.write("Video Link: https://pixabay.com/videos/aurora-borealis-northern-lights-90877/ ")
