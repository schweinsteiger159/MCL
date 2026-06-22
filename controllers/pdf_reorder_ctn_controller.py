from services.pdf_reorder_ctn_service import (
    PdfReorderCtnService
)


class PdfReorderCtnController:

    def __init__(
        self
    ):

        self.service = (
            PdfReorderCtnService()
        )

    def validate(
        self,
        txt_file,
        pdf_files
    ):

        return self.service.validate(
            txt_file,
            pdf_files
        )

    def export_pdf(
        self,
        result
    ):

        return self.service.export_sorted_pdf(
            result.txt_sscc_list,
            result.page_map
        )