import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title = "Mood Quote Generator", page_icon="✨")

st.title("Mood Based Quote Generator")

st.write("Select your mood and get a motivational quote!")

df = pd.read_csv("quotes.csv")

st.sidebar.title("About")
st.sidebar.write("A simple app that gives quotes based on your mood.")

mood = st.selectbox(
    "How are you feeling today?", df["mood"].unique())

if st.button("Get Quote"):
    quote_list = df[df["mood"] == mood]["quote"].tolist()
    quote = random.choice(quote_list)
    st.success("✨" + quote)
