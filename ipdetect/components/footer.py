from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio


class FooterSimple(rio.Component):
    def build(self) -> rio.Component:
        footer_grid = rio.Grid(
            [
                rio.Column(
                    rio.Icon(
                        "material/warehouse", min_height=3, min_width=3, align_x=0
                    ),
                    rio.Column(
                        rio.Text("ACME Industries Ltd."),
                        rio.Text("Providing reliable tech since 1992"),
                        align_y=0,
                        spacing=0.3,
                    ),
                    align_x=0.1,
                ),
                rio.Column(
                    rio.Text("SERVICE", style="heading3", margin_y=1),
                    rio.Column(
                        rio.Text("Branding", justify="left"),
                        rio.Text("Design", justify="left"),
                        rio.Text("Design", justify="left"),
                        rio.Text("Advertisement", justify="left"),
                        align_y=0,
                        spacing=0.5,
                    ),
                    rio.Spacer(),
                ),
                rio.Column(
                    rio.Text("COMPANY", style="heading3", margin_y=1),
                    rio.Column(
                        rio.Text("About Us", justify="left"),
                        rio.Text("Contact", justify="left"),
                        rio.Text("Jobs", justify="left"),
                        rio.Text("Press Kit", justify="left"),
                        align_y=0,
                        spacing=0.5,
                    ),
                    rio.Spacer(),
                ),
                rio.Column(
                    rio.Text("LEGAL", style="heading3", margin_y=1),
                    rio.Column(
                        rio.Text("Terms of Use", justify="left"),
                        rio.Text("Privacy Policy", justify="left"),
                        rio.Text("Cookie Policy", justify="left"),
                        align_y=0,
                        spacing=0.5,
                    ),
                    rio.Spacer(),
                ),
            ],
            align_x=0.5,
            width=50,
            height=10,
            margin_bottom=1,
        )
        return footer_grid


class Footer(rio.Component):
    """
    A simple, static component which displays a footer with the company name and
    website name.
    """

    def build(self) -> rio.Component:
        return rio.Card(
            content=rio.Column(
                # FooterSimple(),
                # rio.Separator(),
                # rio.Row(
                #     rio.Icon("material/warehouse", height=2, width=2),
                #     rio.Text(
                #         "Copyright © 2024 - All right reserved by ACME Industries Ltd",
                #         style="dim",
                #     ),
                #     rio.Spacer(),
                #     rio.Icon("material/grade:fill", height=2, width=2),
                #     rio.Icon("material/bolt:fill", width=2, height=2),
                #     rio.Icon("material/heart_plus:fill", width=2, height=2),
                #     spacing=0.5,
                #     margin=1,
                # ),
                rio.Separator(),
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
