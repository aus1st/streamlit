import streamlit as st
from openai import OpenAI


st.title('Chat-gpt Clone')

client = OpenAI(
    api_key=st.secrets['OPENAI_API_KEY'],
)


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = 'gpt-3.5-turbo'
    
#initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#input
if prompt:= st.chat_input("what's up?"):
    #user prompt into msg history
    st.session_state.messages.append({"role": "user", "content":prompt })
    #display input in chat container
    with st.chat_message('user'):
        st.markdown(prompt)

    #display assistant response in chat container
    with st.chat_message("assistant"):
        message_placeholder= st.empty()
        full_resposne = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]} 
                for m in st.session_state.messages
            ],
            stream=True
        ):
            
            full_resposne += (response.choices[0].delta.content or "")            
            message_placeholder.markdown(full_resposne+ "✒️")
        message_placeholder.markdown(full_resposne)
        #st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content":full_resposne })


