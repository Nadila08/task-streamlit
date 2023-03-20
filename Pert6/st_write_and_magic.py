import streamlit as st
import pandas as pd



st.header("st.write:")

st.write('Hello, *World!* :sunglasses:')

st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))



data_frame= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})



st.write('1 + 1 = ', 2)
st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')



import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)



st.header("magic:")
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x=', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=10)

fig  # 👈 Draw a Matplotlib chart