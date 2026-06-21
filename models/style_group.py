from models.color_group import ColorGroup


class StyleGroup:

    def __init__(self, style=""):

        self.style = style

        self.color_groups = []

    # ==========================================
    # FIND COLOR GROUP
    # ==========================================

    def find_color_group(self, color):

        for cg in self.color_groups:

            if cg.color.upper() == color.upper():

                return cg

        return None

    # ==========================================
    # ADD OR UPDATE SKU
    # ==========================================

    def add_or_update_sku(
        self,
        color,
        desc,
        size,
        qty
    ):

        cg = self.find_color_group(color)

        # ==========================
        # CREATE NEW COLOR
        # ==========================

        if cg is None:

            cg = ColorGroup(
                color=color,
                desc=desc
            )

            self.color_groups.append(cg)

        # ==========================
        # UPDATE SIZE QTY
        # ==========================

        cg.add_or_update_size(
            size=size,
            qty=qty
        )