import fitz
import re

from io import BytesIO

from models.pdf_reorder_result import (
    PdfReorderResult
)


class PdfReorderService:

    def load_txt_sscc(
        self,
        txt_file
    ):

        content = (
            txt_file.read()
            .decode("utf-8")
        )

        result = []

        for line in content.splitlines():

            sscc = re.sub(
                r"\D",
                "",
                line
            )

            if sscc:

                result.append(sscc)

        return result

    def build_page_map(
        self,
        pdf_files
    ):

        page_map = {}

        duplicate = []

        pattern = re.compile(
            r"(\d{18,20})"
        )

        for pdf_file in pdf_files:

            pdf_bytes = pdf_file.read()

            doc = fitz.open(
                stream=pdf_bytes,
                filetype="pdf"
            )

            try:

                for page_index in range(
                    len(doc)
                ):

                    text = doc[
                        page_index
                    ].get_text()

                    match = pattern.search(
                        text
                    )

                    if not match:
                        continue

                    sscc = match.group(1)

                    if sscc in page_map:

                        duplicate.append(
                            sscc
                        )

                        continue

                    page_map[sscc] = (
                        pdf_bytes,
                        page_index
                    )

            finally:

                doc.close()

        return (
            page_map,
            duplicate
        )

    def validate(
        self,
        txt_file,
        pdf_files
        
    ):

        result = PdfReorderResult()
        
        txt_sscc_list = (
            self.load_txt_sscc(
                txt_file
            )
        )
        result.txt_sscc_list = txt_sscc_list
        page_map, duplicate = (
            self.build_page_map(
                pdf_files
            )
        )

        pdf_sscc_set = set(
            page_map.keys()
        )

        txt_sscc_set = set(
            txt_sscc_list
        )

        result.txt_count = len(
            txt_sscc_list
        )

        result.pdf_count = len(
            pdf_sscc_set
        )

        result.matched = sorted(
            list(
                txt_sscc_set
                &
                pdf_sscc_set
            )
        )

        result.missing = sorted(
            list(
                txt_sscc_set
                -
                pdf_sscc_set
            )
        )

        result.unused = sorted(
            list(
                pdf_sscc_set
                -
                txt_sscc_set
            )
        )

        result.duplicate = sorted(
            duplicate
        )

        result.page_map = page_map

        result.pdf_files = pdf_files

        return result

    def export_sorted_pdf(
        self,
        txt_sscc_list,
        page_map
    ):

        output = fitz.open()

        for sscc in txt_sscc_list:

            if sscc not in page_map:
                continue

            pdf_bytes, page_index = (
                page_map[sscc]
            )

            src = fitz.open(
                stream=pdf_bytes,
                filetype="pdf"
            )

            output.insert_pdf(
                src,
                from_page=page_index,
                to_page=page_index
            )

            src.close()

        buffer = BytesIO()

        output.save(buffer)

        output.close()

        buffer.seek(0)

        return buffer