import streamlit as st

# Load HTML
with open("menu.html", 'r', encoding='utf-8') as f:
    html = f.read()

st.set_page_config(layout="wide")
st.markdown(html, unsafe_allow_html=True)
