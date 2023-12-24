import streamlit as st

st.title('Callbacks with Args')

if 'count' not in st.session_state:
    st.session_state.count = 0

increment_param = st.number_input('Set increment',value=1, step=1)

def increment(increment_param):
    st.session_state.count += increment_param


st.button('Increment', on_click=increment, args=(increment_param,))
st.write('Count: ', st.session_state.count)