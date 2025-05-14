import streamlit as st

st.title("🎈My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

col1, col2, col3 = st.columns(3)

with col1
  st.header("kucing")
  st.image("https://static.streamlit.io/examples/cat.jpg")
