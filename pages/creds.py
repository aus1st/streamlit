import streamlit as st

st.write("Db User: ", st.secrets["db_username"])
st.write("Db Password: ", st.secrets["db_password"])

import os

st.write("Db Host", os.environ["db_username"] == st.secrets["db_username"])