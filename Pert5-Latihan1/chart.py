# -*- coding: utf-8 -*-
pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np


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


st.subheader("3-Charts and maps:")


st.write("3A: Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("3B: Plot a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.subheader("6-Caching:")

import streamlit as st

@st.cache  # 👈 This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    return the_output
