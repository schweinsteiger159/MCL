class PdfReorderResult:

    def __init__(self):

        self.txt_count = 0

        self.pdf_count = 0

        self.matched = []

        self.missing = []

        self.unused = []

        self.duplicate = []

        self.page_map = {}

        self.pdf_files = []

        self.txt_sscc_list = []