# services/carton_service.py

import pandas as pd

from models.carton_label import CartonLabel


class CartonService:

    # ==================================================
    # LOAD CARTONS FROM EXCEL
    # ==================================================

    def load_cartons(self, uploaded_file):

        # ==============================================
        # READ EXCEL
        # ==============================================

        df = pd.read_excel(uploaded_file)

        # ==============================================
        # CLEAN COLUMN NAME
        # ==============================================

        df.columns = [
            str(col)
            .strip()
            .upper()
            .replace(" ", "_")
            for col in df.columns
        ]

        # ==============================================
        # REPLACE NaN -> ""
        # ==============================================

        df = df.fillna("")

        # ==============================================
        # STORE RESULT
        #
        # KEY   = CASE_ID
        # VALUE = CartonLabel
        # ==============================================

        cartons = {}

        # ==============================================
        # LOOP ROW
        # ==============================================

        for _, row in df.iterrows():

            # ==========================================
            # READ DATA
            # ==========================================

            po = str(row["PO"]).strip()

            case_id = str(row["CASE_ID"]).strip()

            carton_no = str(row["CARTON_NO"]).strip()

            of = str(row["OF"]).strip()

            style = str(row["STYLE"]).strip()

            color = str(row["COLOR"]).strip()

            size = str(row["SIZE"]).strip()

            dn = str(row["DN"]).strip()

            desc = str(row["DESC"]).strip()

            # ==========================================
            # QTY
            # ==========================================

            qty = row["QTY"]

            if qty == "":
                qty = 0

            qty = int(qty)

            # ==========================================
            # WEIGHT
            # ==========================================

            weight = row["WEIGHT"]

            if weight == "":
                weight = 0

            weight = float(weight)

            # ==========================================
            # SKIP EMPTY CASE ID
            # ==========================================

            if case_id == "":
                continue

            # ==========================================
            # CREATE NEW CARTON
            # ==========================================

            if case_id not in cartons:

                carton = CartonLabel(
                    carton_no=carton_no,
                    po=po,
                    case_id=case_id,
                    dn=dn,
                    of=of,
                    weight=weight
                )

                cartons[case_id] = carton

            else:

                carton = cartons[case_id]

            # ==========================================
            # ADD OR UPDATE SKU
            # ==========================================

            carton.add_or_update_sku(
                style=style,
                color=color,
                desc=desc,
                size=size,
                qty=qty
            )

        # ==============================================
        # RETURN RESULT
        # ==============================================

        return cartons