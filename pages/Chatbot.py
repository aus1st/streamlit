import streamlit as st

st.title('Echo Bot')

#initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#input
if prompt:= st.chat_input("what's up?"):
    #display input in chat history
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content":prompt })


    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content":response })


