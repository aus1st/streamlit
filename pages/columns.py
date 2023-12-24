import streamlit as st

st.header('Columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2:
    st.header('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.header('Rabbit')
    st.image('https://static.streamlit.io/examples/owl.jpg')