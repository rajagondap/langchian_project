import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age:", 0, 100, 25)
if age:
    st.write(f"You are {age} years old.")


oprtions = st.selectbox("Your Fevorite IPL Team:", ["RCB", "RR", "SRH", "GT", "CSK", "MI", "KKR"])
if oprtions:
    st.write(f"You selected: {oprtions}")

oprtions = st.selectbox("Which IPL team got Banned due to Match fixing:", ["RCB", "RR", "SRH", "GT", "CSK", "MI", "KKR", "You Comment on it"])
if oprtions:
    st.write(f"You selected: {oprtions}")


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
st.write("DataFrame")
st.write(df)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame")
    st.write(df)