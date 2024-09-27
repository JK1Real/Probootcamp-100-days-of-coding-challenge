import requests

api_key = "1cb158d3324d8c4cce9493e757c92760"
def moviesfromapi(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"

    headers = {
    "api_key":api_key,
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxY2IxNThkMzMyNGQ4YzRjY2U5NDkzZTc1N2M5Mjc2MCIsInN1YiI6IjY2NzA1MDc5NGM2ODYzNTA2OGQxZTFmMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2yuPCGMB818Wo_MTY1Nl_pTAoOje53urRiX1ajPTKR8"
    }

    response = requests.get(url, headers=headers)

    similar_movie_dictionary = response.json()['results']
    return similar_movie_dictionary


def movie_details(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}?language=en-US"

    headers = {
        "api_key": api_key,
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxY2IxNThkMzMyNGQ4YzRjY2U5NDkzZTc1N2M5Mjc2MCIsInN1YiI6IjY2NzA1MDc5NGM2ODYzNTA2OGQxZTFmMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2yuPCGMB818Wo_MTY1Nl_pTAoOje53urRiX1ajPTKR8"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    movie = response.json()
    return movie


print(moviesfromapi('batman'))
print(movie_details(268))

# class Movie(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(unique=True)
#     year: Mapped[str]
#     description: Mapped[str]
#     rating: Mapped[int]
#     ranking: Mapped[int]
#     review: Mapped[str]
#     img_url: Mapped[str]
