from __future__ import annotations

import rio
from ..components import stats


class Stats(rio.Component):
    def build(self) -> rio.Component:
        stats_info = rio.Row(
            rio.Column(
                rio.Row(
                    rio.Column(
                        stats.stat_title("Total Likes"),
                        stats.stat_value("25.6K", fill=rio.Color.RED),
                        stats.stat_description("21% more than last month"),
                        margin=0.5,
                    ),
                    rio.Icon(
                        "material/favorite:fill",
                        min_height=3,
                        min_width=3,
                        fill=rio.Color.RED,
                    ),
                    spacing=0.5,
                ),
                align_y=0,
            ),
            rio.Separator(),
            rio.Column(
                rio.Row(
                    rio.Column(
                        stats.stat_title("Page Views"),
                        stats.stat_value("2.6M", fill=rio.Color.PINK),
                        stats.stat_description("10% more than last month"),
                        margin=0.5,
                    ),
                    rio.Icon(
                        "material/bolt:fill",
                        min_height=3,
                        min_width=3,
                        fill=rio.Color.PINK,
                    ),
                    spacing=0.5,
                ),
                align_y=0,
            ),
            rio.Separator(),
            rio.Column(
                rio.Row(
                    rio.Column(
                        stats.stat_value("86%", fill=rio.Color.GREEN),
                        stats.stat_title("Tasks Done"),
                        stats.stat_description("31 tasks remaining"),
                        margin=0.5,
                    ),
                    rio.Icon(
                        "material/task:fill",
                        min_height=3,
                        min_width=3,
                        fill=rio.Color.GREEN,
                    ),
                    spacing=0.5,
                ),
                align_y=0,
            ),
            align_x=0.5,
            spacing=2,
            margin=1,
        )
        return stats_info


class StatsPage(rio.Component):
    """
    A sample page, containing recent news articles about the company.
    """

    def build(self) -> rio.Component:
        return rio.Rectangle(
            content=Stats(),
            fill=rio.Color.TRANSPARENT,
            stroke_color=rio.Color.GREY,
            stroke_width=0.1,
            corner_radius=1,
            align_x=0.5,
            margin=1,
        )
