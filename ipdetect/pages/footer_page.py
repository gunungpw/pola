from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio


class CardSimple(rio.Component):
    def build(self) -> rio.Component:
        footer_grid = rio.Grid(
            [
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
            [
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
            height=20,
            width=40,
        )
        return footer_grid


class FooterPage(rio.Component):
    """
    A sample page, containing recent news articles about the company.
    """

    def build(self) -> rio.Component:
        return CardSimple()
