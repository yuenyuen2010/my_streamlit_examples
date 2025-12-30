# Contents of ~/my_app/pages/03_🎉_page3.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time
from PIL import Image
import logging

logger = logging.getLogger(__name__)

st.markdown("# Page 5 🅰️")
st.sidebar.markdown("# Page 5 🅰️")
st.markdown("Reference: https://docs.streamlit.io/library/api-reference/widgets")


"""
# Input widgets
With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.
"""
st.markdown("") # empty line
st.markdown("""---""")


"""
# Button
Display a button widget.
"""
st.markdown("") # empty line

if st.button('Say hello'):
    logger.info("'Say hello' button clicked")
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.markdown("""---""")


"""
# Download Button
Display a download button widget.
"""
st.markdown("") # empty line

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

st.markdown("""---""")


"""
# Checkbox
Display a checkbox widget.
"""
st.markdown("") # empty line

agree = st.checkbox('I agree')

if agree:
    logger.info("User agreed")
    st.write('Great!')

st.markdown("""---""")


"""
# Radio Button
Display a radio button.
"""
st.markdown("") # empty line

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )

st.markdown("""---""")


"""
# SelectBox
Display a select widget.
"""
st.markdown("") # empty line

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.markdown("""---""")


"""
# Multi select
Display a multiselect widget.
"""
st.markdown("")  # empty line

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

logger.debug(f"Multiselect colors: {options}")

st.write('You selected:', options)

st.markdown("""---""")


"""
# slider
Display a slider widget.
"""
st.markdown("")  # empty line

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.markdown("""---""")


"""
# Select slider
Display a slider widget to select items from a list.
"""
st.markdown("")  # empty line

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.markdown("""---""")


"""
# Text Input
Display a single-line text input widget.
"""
st.markdown("")  # empty line

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.markdown("""---""")


"""
# Number Input
Display a numeric input widget.
"""
st.markdown("")  # empty line

number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.markdown("""---""")


"""
# Text Area
Display a multi-line text input widget.
"""
st.markdown("")  # empty line

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')

st.markdown("""---""")



"""
# Date Input
Display a date input widget.
"""
st.markdown("")  # empty line

d = st.date_input(
    "When\'s your birthday",
    date(2019, 7, 6))
st.write('Your birthday is:', d)

st.markdown("""---""")


"""
# Time Input
Display a time input widget.
"""
st.markdown("")  # empty line

t = st.time_input('Set an alarm for', time(8, 45))
st.write('Alarm is set for', t)

st.markdown("""---""")


"""
# File Uploader
Display a file uploader widget.
"""
st.markdown("")  # empty line

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.markdown("""---""")


"""
# Camera Input
Display a widget that returns pictures from the user's webcam.
"""
st.markdown("")  # empty line

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
    st.image(img_file_buffer)

st.markdown("""---""")


"""
# Colour Picker
Display a color picker widget.
"""
st.markdown("")  # empty line

color = st.color_picker('Pick A Color', '#00f900')
logger.debug(f"Color picked: {color}")
st.write('The current color is', color)

st.markdown("""---""")


"""
# Image
Display an image or list of images.
"""
st.markdown("")  # empty line

image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains')

st.markdown("""---""")


"""
# Audio
Display an audio player.
"""
st.markdown("")  # empty line

audio_file = open('sample4.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)


st.markdown("""---""")


"""
# Video
Display a video player.
"""
st.markdown("")  # empty line

video_file = open('sample-mp4-file.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.markdown("""---""")