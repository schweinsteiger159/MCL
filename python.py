import streamlit as st
import pandas as pd

st.title("Webform Upload Excel")

name = st.text_input("Nhập tên đi nè")
age = st.number_input(  "Nhập tuổi", min_value=0, max_value=120)

if st.button("Submit"):
    st.write("Tên:", name)
    st.write("Tuổi:", age)

st.divider()

file = st.file_uploader("Upload file Excel", type=["xlsx"])

if file:
    df = pd.read_excel(file)
    st.write("Dữ liệu Excel:")
    st.dataframe(df)

   #run: streamlit run python.py --server.port 8000 --server.address 0.0.0.0 