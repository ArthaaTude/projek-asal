import streamlit as st
import pandas as pd
import numpy as np

if st.checkbox("data"):
    data = {
        "nama":["agus","prad"],
        "umur":[18,19]
    }
    hasil = pd.DataFrame(data)
    st.write(hasil)
    option = st.selectbox(
        "pilihan",
        data["nama"],
    )
    option
else:
    if st.checkbox("data lainnya"):    
        if st.checkbox("data map"):
            data_map = pd.DataFrame(
                np.random.randn(1000,2) / [50,50] + [37.36,-122.4],
                columns=['lat','lon']
            )
            st.map(data_map)
        if st.checkbox("data line chart"):
            data_line_chart = pd.DataFrame(
                np.random.randn(10,2),
                columns=['x','y']
            )
            st.line_chart(data_line_chart)
        if st.checkbox("slider"):
            a = st.slider("x")
            st.write(a+a)
        if st.checkbox("nama"):
            st.text_input("nama:",key="nama")
            st.session_state.nama