from models.style_group import StyleGroup


class CartonLabel:

    def __init__(
        self,
        carton_no="",
        po="",
        case_id="",
        dn="",
        of="",
        weight=0
    ):

        self.carton_no = carton_no
        self.po = po
        self.case_id = case_id
        self.dn = dn
        self.of = of
        self.weight = weight

        self.style_groups = []

    # ==========================================
    # FIND STYLE GROUP
    # ==========================================

    def find_style_group(self, style):

        for sg in self.style_groups:

            if sg.style.upper() == style.upper():

                return sg

        return None

    # ==========================================
    # ADD OR UPDATE SKU
    # ==========================================

    def add_or_update_sku(
        self,
        style,
        color,
        desc,
        size,
        qty
    ):

        sg = self.find_style_group(style)

        if sg is None:

            sg = StyleGroup(style)

            self.style_groups.append(sg)

        sg.add_or_update_sku(
            color=color,
            desc=desc,
            size=size,
            qty=qty
        )