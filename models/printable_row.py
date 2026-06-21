class PrintableRow:

    def __init__(
        self,
        style="",
        color="",
        size="",
        qty=0,
        show_style=True,
        show_color=True,
        is_style_end=False
    ):

        self.style = style
        self.color = color
        self.size = size
        self.qty = qty

        self.show_style = show_style
        self.show_color = show_color

        self.is_style_end = is_style_end