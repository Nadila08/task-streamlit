
import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.header("st.set_page_config:")



st.header("st.echo")

st.caption("Example-1:")
import streamlit as st

with st.echo():
    st.write('This code will be printed')


st.caption("Example-2:")
import streamlit as st

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')


st.header("st.help")

st.caption("Example-1:")

import streamlit as st
import pandas

st.help(pandas.DataFrame)


st.caption("Example-2:")
import streamlit as st
my_poorly_documented_number=10
x = my_poorly_documented_number
st.help(x)


st.header("st.experimental_show, similar to st.write()")
import streamlit as st
import pandas as pd

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
st.experimental_show(dataframe)
