import streamlit as st
import random
import time


st.title('Simple Bot')

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
        message_placeholder= st.empty()
        full_resposne = ""
        assistant_response = random.choice([
            "Hi there! How can i help you today?",
            "Hi, human! Is there anything i can help you with?",
            "Do you need help with something? I'm here to help."
        ])

        for chunk in assistant_response.split():
            full_resposne += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_resposne+ "✒️")
        message_placeholder.markdown(full_resposne)
        #st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content":full_resposne })


