import streamlit as st
import numpy as np

st.header('Container')

with st.container():
    st.write('This is container area')

    st.bar_chart(np.random.rand(50,3))
    st.warning('inside container')

st.write('This is outside container')
st.write('This is outside container')
