import streamlit as st

tambah = st.sidebar.checkbox(
    "pilih:",
    ("email","no hp")
)

add_slibar = st.sidebar.slider(
    "pilihan",
    0.0,100.0, (25.0,75.0)
)