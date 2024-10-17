from __future__ import annotations
import rio
from .stats_page import Stats


class ComponentPage(rio.Component):
    """
    A sample page, containing recent news articles about the company.
    """

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Rectangle(
                content=Stats(),
                fill=rio.Color.TRANSPARENT,
                stroke_color=rio.Color.GREY,
                stroke_width=0.1,
                corner_radius=1,
                align_x=0.5,
                margin=1,
            ),
        )
