import streamlit as st

st.title("Meu primeiro Streamlit")
st.header("testando, oi..")
nome = st.text_input("Digite seu nome", "")
st.write("bem vindos!")

if nome != "":
    st.write(f"{nome}, deixe seu like! e um comentário.")
