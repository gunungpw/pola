import rio


class FooterOneline(rio.Component):
    def build(self) -> rio.Component:
        return rio.Row(
            rio.Icon("material/warehouse", min_height=2, min_width=2),
            rio.Text(
                "Copyright © 2024 - All right reserved by ACME Industries Ltd",
                style="dim",
            ),
            rio.Spacer(),
            rio.Icon("material/grade:fill", min_height=2, min_width=2),
            rio.Icon("material/bolt:fill", min_width=2, min_height=2),
            rio.Icon("material/heart_plus:fill", min_width=2, min_height=2),
            spacing=0.5,
            margin=1,
        )
