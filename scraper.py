import bs4
import requests
import datetime


class Scraper:
    def __init__(self, base_url: str) -> [(str, str)]:
        self.__base_url = base_url

    def scrape(self, date: datetime.datetime):

        response = requests.get(self.__base_url + date.strftime("%Y-%m-%d"))
        soup = bs4.BeautifulSoup(response.text, features="html.parser")

        res = soup.select("ol.chart-list__elements > li.chart-list__element span.chart-element__information")
        return [(song_information.select_one(".chart-element__information__artist").text,
                       song_information.select_one(".chart-element__information__song").text)
                      for song_information in res]

