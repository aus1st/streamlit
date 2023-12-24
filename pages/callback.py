import streamlit as st

st.title('Callback')

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1

st.button('Increment', on_click=increment)
st.write('Count: ', st.session_state.count)