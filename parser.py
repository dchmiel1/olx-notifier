from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass
class OlxOffer:
    id: str
    name: str
    loc: str
    date: str
    href: str

    def __str__(self):
        return f"{self.id},{self.name},{self.date},{self.loc},{self.href}"

    @classmethod
    def _retrieve_offer_name(cls, div):
        name_el = div.find(class_="css-1wxaaza")
        if name_el is None:
            return None
        return name_el.text

    @classmethod
    def _retrieve_offer_location_and_date(cls, div):
        loc_and_date_el = div.find(class_="css-1mwdrlh")
        if loc_and_date_el is None:
            return None, None
        return loc_and_date_el.text.split("-", 1)

    @classmethod
    def _retrieve_offer_href(cls, div):
        href_el = div.find(class_="css-z3gu2d")
        if href_el is None:
            return None
        return "https://www.olx.pl" + href_el["href"]

    @classmethod
    def parse(cls, offer_div):
        id = offer_div["id"]
        name = cls._retrieve_offer_name(offer_div)
        loc, date = cls._retrieve_offer_location_and_date(offer_div)
        href = cls._retrieve_offer_href(offer_div)
        return OlxOffer(id, name, loc, date, href)


class OlxPageParser:
    def __init__(self, page_html):
        self.page_html = page_html

    def _get_offers_grid(self):
        soup = BeautifulSoup(self.page_html, features="html.parser")
        grid = soup.find(class_="css-j0t2x2")
        return grid

    def _parse_grid(self, grid):
        offers = []
        for div in grid:
            if not div.has_attr("data-cy"):
                continue
            if div.find(text="Wyróżnione") is not None:
                continue
            offer = OlxOffer.parse(div)
            offers.append(offer)
        return offers

    def retrieve_offers(self):
        grid = self._get_offers_grid()
        offers = self._parse_grid(grid)
        return offers
