from __future__ import annotations

from typing import *  # type: ignore

import rio


class HomePage(rio.Component):
    """
    A sample page, containing a greeting and some testimonials.
    """

    def build(self) -> rio.Component:
        return rio.Column(rio.Text("RIO COMPONENT", style="heading1"))
