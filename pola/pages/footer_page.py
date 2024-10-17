from __future__ import annotations

from pathlib import Path

import rio

from pola.components.footer_grid import FooterGrid
from pola.components.footer_oneline import FooterOneline
from pola.components.footer_simple import FooterSimple


class FooterPage(rio.Component):
    """
    A sample page, containing recent news articles about the company.
    """

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Text("Footer Grid", style="heading1", margin_top=3),
            FooterGrid(),
            rio.Revealer(
                header="Footer Grid",
                content=rio.CodeBlock(
                    code=f"{open(Path(__file__).parent.joinpath("..", "components", "footer_grid.py")).read()}",
                    language="python",
                ),
            ),
            rio.Text("Footer Simple", style="heading1", margin_top=3),
            FooterSimple(),
            rio.Revealer(
                header="Footer Simple",
                content=rio.CodeBlock(
                    code=f"{open(Path(__file__).parent.joinpath("..", "components", "footer_simple.py")).read()}",
                    language="python",
                ),
            ),
            rio.Text("Footer Oneline", style="heading1", margin_top=3),
            FooterOneline(),
            rio.Revealer(
                header="Footer Oneline",
                content=rio.CodeBlock(
                    code=f"{open(Path(__file__).parent.joinpath("..", "components", "footer_oneline.py")).read()}",
                    language="python",
                ),
            ),
        )
