from __future__ import annotations

import rio


@rio.page(url_segment="", name="Pola")
class HomePage(rio.Component):
    """
    A sample page, containing a greeting and some testimonials.
    """

    def build(self) -> rio.Component:
        return rio.Column(rio.Text("RIO COMPONENT", style="heading1", justify="center"))
