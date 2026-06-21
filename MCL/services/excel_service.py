# services/excel_service.py

import pandas as pd

class ExcelService:

    def read_excel(self, file):

        df = pd.read_excel(file)

        return df