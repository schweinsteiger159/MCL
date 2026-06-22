from services.pdf_reorder_service import (
    PdfReorderService
)


class PdfReorderController:

    def __init__(self):

        self.service = (
            PdfReorderService()
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
            result.page_map,
            result.txt_sscc_list
        )
