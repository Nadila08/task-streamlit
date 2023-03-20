import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Display Element")





st.subheader("st.dataframe:")
st.caption("* Column sorting")
st.caption("* Column resizing")
st.caption("* Table (height, width) resizing")
st.caption("* Search")
st.caption("* Copy to clipboard")





df = pd.DataFrame(
   np.random.randn(5, 5),
   columns=('col %d' % i for i in range(5)))

st.dataframe(df)  # Same as st.write(df)



df = pd.DataFrame(
   np.random.randn(3, 3),
   columns=('col %d' % i for i in range(3)))

st.dataframe(df.style.highlight_max(axis=0))




# Cache the dataframe so it's only loaded once
@st.experimental_memo
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)


st.subheader("st.dataframe:")
st.caption("Display a static table.")
df = pd.DataFrame(
   np.random.randn(3, 3),
   columns=('col %d' % i for i in range(3)))

st.table(df)


st.subheader("st.metric:")
st.caption("Display a metric in big bold font, with an optional indicator of how the metric changed.")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")


st.subheader("st.json:")
st.caption("Display object or string as a pretty-printed JSON string.")
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

