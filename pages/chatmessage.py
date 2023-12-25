import streamlit as st
import numpy as np

message = st.chat_message("assistant")
message.write("hello, how may i help you")
message.bar_chart(np.random.randn(30,4))