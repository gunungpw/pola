from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio
from pathlib import Path


class CardSimple(rio.Component):
    def build(self) -> rio.Component:
        return rio.Card(
            rio.Column(
                rio.Rectangle(
                    fill=rio.ImageFill(
                        image=Path(self.session.assets / "shoes.webp"),
                        fill_mode="stretch",
                    ),
                    min_height=15,
                    corner_radius=(0.5, 0.5, 0, 0),
                    min_width=20,
                    align_y=0,
                    align_x=0,
                ),
                rio.Text(
                    "Shoes!",
                    justify="left",
                    style="heading1",
                    align_y=0,
                    align_x=0,
                    margin_top=1,
                    margin_left=1,
                ),
                rio.Text(
                    "If a dog chews shoes",
                    style="text",
                    justify="left",
                    align_y=0,
                    align_x=0,
                    margin_top=0.5,
                    margin_left=1,
                ),
                rio.Row(
                    rio.Spacer(),
                    rio.Button(
                        "Buy",
                        shape="rectangle",
                        margin=0.5,
                        align_x=0,
                    ),
                    align_y=0,
                    margin_top=1,
                ),
                rio.Spacer(),
                align_x=0,
                align_y=0,
            ),
            color=rio.Color.GREY,
            align_x=0.5,
            align_y=0,
            margin=0.5,
            corner_radius=0.5,
        )


class NewsPage(rio.Component):
    """
    A sample page, containing recent news articles about the company.
    """

    def build(self) -> rio.Component:
        return rio.Row(CardSimple(), CardSimple(), CardSimple(), spacing=0.5)
