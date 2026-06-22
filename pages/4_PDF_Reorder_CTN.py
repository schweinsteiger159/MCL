import streamlit as st

from controllers.pdf_reorder_ctn_controller import (
    PdfReorderCtnController
)

# ==========================================
# CONTROLLER
# ==========================================

controller = (
    PdfReorderCtnController()
)

# ==========================================
# TITLE
# ==========================================

st.title(
    "PDF Reorder CTN"
)

# ==========================================
# FILE UPLOAD
# ==========================================

txt_file = st.file_uploader(
    "TXT File",
    type=["txt"]
)

pdf_files = st.file_uploader(
    "PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

# ==========================================
# VALIDATE
# ==========================================

if st.button(
    "Validate"
):

    if txt_file is None:

        st.error(
            "Please upload TXT file."
        )

    elif not pdf_files:

        st.error(
            "Please upload PDF files."
        )

    else:

        result = controller.validate(
            txt_file,
            pdf_files
        )

        st.session_state[
            "ctn_validation_result"
        ] = result

# ==========================================
# SHOW RESULT
# ==========================================

if (
    "ctn_validation_result"
    in st.session_state
):

    result = st.session_state[
        "ctn_validation_result"
    ]

    # ======================================
    # SUMMARY
    # ======================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Matched",
        len(result.matched)
    )

    col2.metric(
        "Missing",
        len(result.missing)
    )

    col3.metric(
        "Unused",
        len(result.unused)
    )

    col4.metric(
        "Duplicate",
        len(result.duplicate)
    )

    # ======================================
    # MATCHED
    # ======================================

    with st.expander(
        f"Matched ({len(result.matched)})"
    ):
        st.write(
            result.matched
        )

    # ======================================
    # MISSING
    # ======================================

    with st.expander(
        f"Missing ({len(result.missing)})"
    ):
        st.write(
            result.missing
        )

    # ======================================
    # UNUSED
    # ======================================

    with st.expander(
        f"Unused ({len(result.unused)})"
    ):
        st.write(
            result.unused
        )

    # ======================================
    # DUPLICATE
    # ======================================

    with st.expander(
        f"Duplicate ({len(result.duplicate)})"
    ):
        st.write(
            result.duplicate
        )

    # ======================================
    # STATUS
    # ======================================

    is_valid = (
        len(result.missing) == 0
        and
        len(result.unused) == 0
        and
        len(result.duplicate) == 0
    )

    if is_valid:

        st.success(
            "Validation Passed"
        )

    else:

        st.warning(
            "Validation Issues Found"
        )

        st.info(
            "You can still export if needed."
        )

    # ======================================
    # EXPORT
    # ======================================

    if st.button(
        "Confirm And Export PDF"
    ):

        pdf_buffer = (
            controller.export_pdf(
                result
            )
        )

        st.download_button(
            label="Download Sorted PDF",
            data=pdf_buffer,
            file_name="ctn_sorted.pdf",
            mime="application/pdf"
        )