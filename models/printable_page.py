class PrintablePage:

    def __init__(
        self,
        carton,
        page_no=1,
        total_pages=1
    ):

        self.carton = carton

        self.page_no = page_no
        self.total_pages = total_pages

        self.rows = []