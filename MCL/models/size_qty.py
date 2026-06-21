class SizeQty:

    def __init__(
        self,
        size="",
        qty=0
    ):

        self.size = size
        self.qty = qty

    def increase_qty(self, value):

        self.qty += value