from __future__ import annotations

from pathlib import Path

import rio

from pola import pages

# Define a theme for Rio to use.
#
# You can modify the colors here to adapt the appearance of your app or website.
# The most important parameters are listed, but more are available! You can find
# them all in the docs
#
# https://rio.dev/docs/api/theme
theme = rio.Theme.from_colors(
    primary_color=rio.Color.from_hex("01dffdff"),
    secondary_color=rio.Color.from_hex("0083ffff"),
    mode="dark",
)


# Create the Rio app
app = rio.App(
    name="Pola",
    pages=[
        rio.ComponentPage(
            name="Home",
            url_segment="",
            build=pages.HomePage,
        ),
        rio.ComponentPage(
            name="NewsPage",
            url_segment="news-page",
            build=pages.NewsPage,
        ),
        rio.ComponentPage(
            name="Footer",
            url_segment="footer-page",
            build=pages.FooterPage,
        ),
        rio.ComponentPage(
            name="Stats",
            url_segment="stats-page",
            build=pages.StatsPage,
        ),
    ],
    # You can optionally provide a root component for the app. By default,
    # a simple `rio.PageView` is used. By providing your own component, you
    # can create components which stay put while the user navigates between
    # pages, such as a navigation bar or footer.
    #
    # When you do this, make sure your component contains a `rio.PageView`
    # so the currently active page is still visible.
    build=pages.RootPage,
    theme=theme,
    assets_dir=Path(__file__).parent.joinpath("assets"),
)
