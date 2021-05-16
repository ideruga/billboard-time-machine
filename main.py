import datetime
from dateutil.relativedelta import relativedelta
from scraper import Scraper
from spotify import Spotify
import random


def rand_date():
    to_date = datetime.datetime.now()
    from_date = to_date - relativedelta(years=20)
    delta = to_date - from_date
    rnd = random.randint(0, delta.days)
    return from_date + relativedelta(days=rnd)


def fill_playlist():
    scraper = Scraper("https://www.billboard.com/charts/hot-100/")
    song_list = scraper.scrape(rand_date())
    spotify = Spotify()
    playlist = spotify.get_playlist()
    print(f"created playlist: {playlist}")
    song_ids = spotify.get_song_ids(song_list)
    spotify.fill_with_songs(playlist, song_ids)


fill_playlist()
