# pages/2_Extra_Label.py

import streamlit as st

from services.carton_service import CartonService
from services.word_service import WordService

# ==================================================
# SERVICES
# ==================================================

carton_service = CartonService()

word_service = WordService()

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Extra Label",
    layout="wide"
)

# ==================================================
# TITLE
# ==================================================

st.title("Extra Label")

# ==================================================
# UPLOAD FILE
# ==================================================

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

# ==============================================
# PROCESS FILE
# ==============================================

if uploaded_file is not None:

    # ==========================================
    # LOAD CARTONS
    # ==========================================

    cartons = carton_service.load_cartons(
        uploaded_file
    )

    st.success("Load Excel Success")

    st.write(
        f"Total Cartons : {len(cartons)}"
    )

    # ==========================================
    # GENERATE WORD
    # ==========================================

    word_buffer = word_service.export_word(
        cartons
    )

    # ==========================================
    # DOWNLOAD BUTTON
    # ==========================================

    st.download_button(
        label="📥 Export Word File",
        data=word_buffer,
        file_name="carton_label.docx",
        mime=(
            "application/"
            "vnd.openxmlformats-officedocument"
            ".wordprocessingml.document"
        )
    )

    # ==========================================
    # SHOW DATA
    # ==========================================

    for case_id, carton in cartons.items():

        st.divider()

        st.subheader(
            f"CASE ID : {carton.case_id}"
        )

        st.write(f"PO : {carton.po}")

        st.write(
            f"CARTON NO : {carton.carton_no}"
        )

        st.write(f"OF : {carton.of}")

        st.write(f"DN : {carton.dn}")

        st.write(
            f"WEIGHT : {carton.weight}"
        )

        # ======================================
        # STYLE GROUP
        # ======================================

        for style_group in carton.style_groups:

            st.markdown(
                f"### STYLE : {style_group.style}"
            )

            # ==================================
            # COLOR GROUP
            # ==================================

            for color_group in (
                style_group.color_groups
            ):

                st.write(
                    f"COLOR : {color_group.color}"
                )

                st.write(
                    f"DESC : {color_group.desc}"
                )

                # ==============================
                # SIZE QTY
                # ==============================

                for size_qty in (
                    color_group.size_qty_list
                ):

                    st.write(
                        f"SIZE : {size_qty.size}"
                        f" | "
                        f"QTY : {size_qty.qty}"
                    )
