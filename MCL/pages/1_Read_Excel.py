# pages/1_Read_Excel.py

import streamlit as st
from controllers.excel_controller import ExcelController

controller = ExcelController()

st.title("Đọc file Excel")

uploaded_file = st.file_uploader(
    "Upload file",
    type=["xlsx"]
)

if uploaded_file:

    df = controller.read_excel(uploaded_file)

    st.dataframe(df)