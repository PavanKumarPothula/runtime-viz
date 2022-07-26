import tmdbsimple as tmdb
import pprint


def setupDiscover() -> tmdb.Discover:
    from keys import TMDB_KEY
    tmdb.API_KEY = TMDB_KEY
    return tmdb.Discover()


def fetcher(start_year: str = '2000-01-01', end_year: str = '2022-01-01',  vote_average_gte: int = 5, sort_by: str = 'release_date.desc'):
    discoverer = setupDiscover()
    response = discoverer.movie(start_year=start_year,
                                end_year=end_year, vote_average_gte=vote_average_gte, sort_by=sort_by)

    # TODO: find all the movies in all the pages.
  
    for result in discoverer.results:
        pprint.pprint(result['title'])

    pprint.pprint(len(discoverer.results))


if __name__ == "__main__":
    fetcher()
