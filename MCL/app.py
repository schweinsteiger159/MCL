import streamlit as st

#run: streamlit run app.py or streamlit run MCL/app.py

st.set_page_config(
    page_title="Warehouse System",
    layout="wide"
)

st.title("Warehouse Management System")

st.page_link(
    "pages/1_Read_Excel.py",
    label="📄 Đọc file Excel"
)


st.page_link(
    "pages/2_Extra_Label.py",
    label="🏷️ Extra Label",
    icon="🏷️"
)
