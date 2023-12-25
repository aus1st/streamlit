import streamlit as  st

st.title("Chat Input")

if "data" not in st.session_state:
    st.session_state.data = []

prompt = st.chat_input("Say Something")


if prompt:
    st.session_state.data.append(prompt)
st.write(st.session_state.data)