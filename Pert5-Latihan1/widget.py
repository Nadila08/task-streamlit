import streamlit as st
import pandas as pd
import numpy as np

"""
# My first app
Here's our first attempt at using data to create a table:
"""
st.subheader("1-Magic:")
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


st.subheader("2-Write a data frame:")


st.write("2A: Manual dataframe")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.write("2B: Random dataframe")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

 
st.write("2C: Using Panda Styler")
dataframe = pd.DataFrame(
    np.random.randn(7, 7),
    columns=('col %d' % i for i in range(7)))

st.dataframe(dataframe.style.highlight_max(axis=0))


st.write("2D: Static table generation")
dataframe = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %d' % i for i in range(5)))
st.table(dataframe)

st.subheader("4-Widgets:")

st.write("4A: Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.write("4B: Text input")
st.text_input("Your name", key="name")
# You can access the value at any point with:
#st.session_state.name


st.write("4C: Checkbox")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(5, 2),
       columns=['a', 'b'])

    chart_data



st.write("4D: Selectbox")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.subheader("6-Caching:")

"""
The Streamlit cache allows your app to execute 
quickly even when loading data from the web, manipulating large datasets, or performing expensive computations.
"""

import streamlit as st

@st.cache  # 👈 This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    return the_output
