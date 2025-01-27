import streamlit as st

st.title("kalkulator")

panjang = st.number_input("nilai",0)
lebar = st.number_input("nilaii",0)
pilihan = st.radio("pilihan",("tambah","kali"))

if st.button("hitung"):
    if pilihan == "tambah":
        hasil = panjang + lebar
    elif pilihan == "kali":
        hasil = panjang * lebar
    st.write("hasil",hasil)