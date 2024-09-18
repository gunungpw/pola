from __future__ import annotations

from typing import *  # type: ignore
from typing import Iterable, Mapping

import httpx
import rio


class HomePage(rio.Component):
    """
    A sample page, containing a greeting and some testimonials.
    """

    ip_info: Mapping[str, Iterable[str] | None] = {}

    def _on_get_ip(self) -> dict:
        information: Mapping[str, Iterable[str] | None] = {
            "info": [],
            "data": [],
        }
        info = httpx.get("http://ip-api.com/json/")
        for el in info.json():
            information["info"].append(el)
            information["data"].append(info.json()[el])
        return information

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Row(
                rio.Spacer(),
                rio.Button("GET IP", shape="rectangle", on_press=self._on_get_ip),
                rio.Spacer(),
                proportions=[0.3, 0.4, 0.3],
                margin=1,
                spacing=1,
                height=1,
            ),
            rio.Table(data=self._on_get_ip(), show_row_numbers=False, width=10),
            width="grow",
        )
