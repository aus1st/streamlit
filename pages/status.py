import streamlit as st
import time
with st.status('Downloading ...', expanded=True) as status:
    st.write('Search for Data')
    time.sleep(2)
    st.write('Found URL')
    time.sleep(1)
    st.write('Downloading Data...')
    time.sleep(1)
    status.update(label='Downloading Completed!', state="complete", expanded=False)

