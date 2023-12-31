import streamlit as st
import time

st.header('Empty')

with st.empty():
    for seconds in range(10):
        st.write(f"⌛{seconds} seconds elapsed...")
        time.sleep(1)
    st.write('✔️ Done!')