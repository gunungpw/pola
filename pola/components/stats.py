import rio
from typing import Literal


def stat_title(text: str, margin_bottom: float = 0.5) -> rio.Text:
    return rio.Text(text, margin_bottom=margin_bottom)


def stat_value(
    text: str,
    font_weight: Literal["bold", "normal"] = "bold",
    font_size: float = 3,
    fill: rio.Color = rio.Color.RED,
) -> rio.Text:
    return rio.Text(
        text,
        style=rio.TextStyle(font_weight=font_weight, font_size=font_size, fill=fill),
    )


def stat_description(
    text: str,
    font_size: float = 0.75,
    italic: bool = True,
    fill: rio.Color = rio.Color.GREY,
) -> rio.Text:
    return rio.Text(
        text,
        style=rio.TextStyle(font_size=font_size, italic=italic, fill=fill),
    )
