import streamlit as st

pg = st.navigation([
    st.Page(
        "pages/1_Read_Excel.py",
        title="Test thử đọc file excel"
    ),
    st.Page(
        "pages/2_Extra_Label.py",
        title="Barbours Label Detail"
    ),
    st.Page(
        "pages/3_PDF_Reorder.py",
        title="Caleres sort theo SSCC"
    ),
    
    st.Page(
        "pages/4_PDF_Reorder_CTN.py",
        title="APS sort theo carton NO."
    )

])

pg.run()