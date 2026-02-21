import requests

ANILIST_URL = "https://graphql.anilist.co"

def fetch_anime_details(name):
    query = """
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        id
        title { romaji }
        genres
        coverImage { large }
      }
    }
    """

    variables = {"search": name}

    response = requests.post(
        ANILIST_URL,
        json={"query": query, "variables": variables}
    )

    data = response.json()
    return data["data"]["Media"]


def recommend_anime(name):
    anime = fetch_anime_details(name)

    if not anime:
        return []

    genres = anime["genres"]

    # Get anime from same first genre
    genre_query = """
    query ($genre: String) {
      Page(perPage: 5) {
        media(genre_in: [$genre], type: ANIME, sort: POPULARITY_DESC) {
          title { romaji }
          coverImage { large }
        }
      }
    }
    """

    variables = {"genre": genres[0]}

    response = requests.post(
        ANILIST_URL,
        json={"query": genre_query, "variables": variables}
    )

    results = response.json()["data"]["Page"]["media"]

    recommendations = []
    for item in results:
        recommendations.append(
            (item["title"]["romaji"], item["coverImage"]["large"])
        )

    return recommendations

def get_popular_anime():
    url = "https://graphql.anilist.co"

    query = '''
    query {
      Page(perPage: 50) {
        media(type: ANIME, sort: POPULARITY_DESC) {
          id
          title {
            romaji
          }
        }
      }
    }
    '''

    response = requests.post(url, json={'query': query})
    data = response.json()

    anime_list = []
    for anime in data['data']['Page']['media']:
        anime_list.append(anime['title']['romaji'])

    return anime_list