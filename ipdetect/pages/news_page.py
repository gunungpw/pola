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
                    height=20,
                    corner_radius=(0.5, 0.5, 0, 0),
                    width=20,
                    align_y=0,
                ),
                rio.Text(
                    "Shoes!",
                    justify="left",
                    style="heading1",
                    height="natural",
                    align_y=0,
                    margin_top=1,
                    margin_left=1,
                ),
                rio.Text(
                    "If a dog chews shoes whose shoes does he choose?",
                    style="text",
                    justify="left",
                    height="natural",
                    margin_top=0.5,
                    margin_left=1,
                ),
                rio.Row(
                    rio.Spacer(),
                    rio.Button(
                        "Buy", width="natural", height="natural", shape="rectangle"
                    ),
                    rio.Spacer(),
                    proportions=[1, 0.5, 0.1],
                    align_x=0,
                    align_y=0,
                    width=20,
                    margin_top=1,
                ),
                rio.Spacer(),
                height=30,
                width=20,
                align_x=0,
                align_y=0,
            ),
            color=rio.Color.GREY,
            align_x=0.5,
            align_y=0,
            margin=1,
            corner_radius=0.5,
        )


class NewsPage(rio.Component):
    """
    A sample page, containing recent news articles about the company.
    """

    def build(self) -> rio.Component:
        return rio.Row(CardSimple(), CardSimple(), CardSimple(), spacing=7)
