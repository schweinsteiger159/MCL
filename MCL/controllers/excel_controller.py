# controllers/excel_controller.py

from services.excel_service import ExcelService

class ExcelController:

    def __init__(self):
        self.service = ExcelService()

    def read_excel(self, file):

        return self.service.read_excel(file)