from models.size_qty import SizeQty


class ColorGroup:

    def __init__(
        self,
        color="",
        desc=""
    ):

        self.color = color
        self.desc = desc

        self.size_qty_list = []

    # ==========================================
    # FIND SIZE
    # ==========================================

    def find_size_qty(self, size):

        for sq in self.size_qty_list:

            if sq.size.upper() == size.upper():

                return sq

        return None

    # ==========================================
    # ADD OR UPDATE SIZE
    # ==========================================

    def add_or_update_size(
        self,
        size,
        qty
    ):

        sq = self.find_size_qty(size)

        if sq is None:

            sq = SizeQty(
                size=size,
                qty=qty
            )

            self.size_qty_list.append(sq)

        else:

            sq.increase_qty(qty)
