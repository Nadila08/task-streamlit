import streamlit as st
import pandas as pd
import numpy as np

st.title("Input Widget")

st.subheader("st.button:")
import streamlit as st

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


st.subheader("st.download_button:")

#Example-1:
import streamlit as st

my_large_df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [19.07, 72.87],columns=['latitude', 'longitude'])



@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)


import streamlit as st
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)


import streamlit as st
binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('Download binary file', binary_contents)



st.subheader("st.checkbox:")
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')


st.subheader("st.radio:")
genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")



# Example-2: 
import streamlit as st
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


st.subheader("st.selectbox:")

st.caption("Example-1:")
import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


st.caption("Example-2:")
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disa")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visi",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "Which one for contact?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visi,
        disabled=st.session_state.disa,
    )


st.subheader("st.multiselect:")
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)




st.subheader("st.slider:")

st.caption("Example-1:")
import streamlit as st
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


st.caption("Example-2:")
import streamlit as st
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


st.caption("Example-3:")
import streamlit as st
from datetime import time
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)



st.caption("Example-4:")
import streamlit as st
from datetime import datetime
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


st.subheader("st.select_slider")

st.caption("Example-1:")
import streamlit as st
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)


st.caption("Example-2:")
import streamlit as st
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


st.subheader("st.text_input:")

st.caption("Example-1:")
import streamlit as st
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)



st.caption("Example-2:")
import streamlit as st
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disaaa")
    st.radio(
        "Set text input label visibility 👉",
        key="visiii",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visiii,
        disabled=st.session_state.disa,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)


st.subheader("st.number_input:")
import streamlit as st

number = st.number_input('Insert a number')
st.write('The current number is ', number)





st.subheader("st.text_area:")
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', txt)


st.subheader("st.date_input:")
import datetime
import streamlit as st

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)



st.subheader("st.time_input:")
import datetime
import streamlit as st

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


st.subheader("st.file_uploader:")
st.caption("Example-1: Only One File")
import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)



st.caption("Example-2: Multiple File")
import streamlit as st
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)




st.subheader("st.color_picker:")
import streamlit as st

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)




