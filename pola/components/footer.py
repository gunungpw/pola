from __future__ import annotations

import rio


class Footer(rio.Component):
    """
    A simple, static component which displays a footer with the company name and
    website name.
    """

    def build(self) -> rio.Component:
        return rio.Card(
            content=rio.Column(
                rio.Row(
                    rio.Text(
                        "Copyright © 2024 - All right reserved by ACME Industries Ltd",
                        justify="center",
                    ),
                    spacing=1,
                    margin=1,
                    align_x=0.5,
                ),
            ),
            color="hud",
            corner_radius=0,
        )
