import fitz
import re

from io import BytesIO

from models.pdf_reorder_result import (
    PdfReorderResult
)


class PdfReorderCtnService:

    def load_ctn_list(
        self,
        txt_file
    ):

        content = (
            txt_file.read()
            .decode("utf-8")
        )

        result = []

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            result.append(
                int(line)
            )

        return result

    def build_page_map(
        self,
        pdf_files
    ):

        page_map = {}

        duplicate = []

        pattern = re.compile(
            r"CTN:\s*(\d+)\s+of",
            re.IGNORECASE
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

                    page = doc[
                        page_index
                    ]

                    text = page.get_text()

                    match = pattern.search(
                        text
                    )

                    if not match:
                        continue

                    carton_no = int(
                        match.group(1)
                    )

                    if carton_no in page_map:

                        duplicate.append(
                            carton_no
                        )

                        continue

                    page_map[
                        carton_no
                    ] = (
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

        txt_ctn_list = (
            self.load_ctn_list(
                txt_file
            )
        )

        result.txt_sscc_list = (
            txt_ctn_list
        )

        page_map, duplicate = (
            self.build_page_map(
                pdf_files
            )
        )

        txt_set = set(
            txt_ctn_list
        )

        pdf_set = set(
            page_map.keys()
        )

        result.txt_count = len(
            txt_ctn_list
        )

        result.pdf_count = len(
            pdf_set
        )

        result.matched = sorted(
            list(
                txt_set & pdf_set
            )
        )

        result.missing = sorted(
            list(
                txt_set - pdf_set
            )
        )

        result.unused = sorted(
            list(
                pdf_set - txt_set
            )
        )

        result.duplicate = sorted(
            duplicate
        )

        result.page_map = (
            page_map
        )

        return result

    def export_sorted_pdf(
        self,
        txt_ctn_list,
        page_map
    ):

        output = fitz.open()

        for carton_no in txt_ctn_list:

            if carton_no not in page_map:
                continue

            pdf_bytes, page_index = (
                page_map[
                    carton_no
                ]
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