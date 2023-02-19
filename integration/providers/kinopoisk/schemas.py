"""Kinopoisk response schemas."""
from pydantic import BaseModel


class ExternalData(BaseModel):
    """External data schema."""
    kpHD: str | None
    imdb: str
    _id: str


class Docs(BaseModel):
    """Docs schema"""
    externalId: ExternalData


class MoviesResponse(BaseModel):
    """Movies response schema"""
    docs: list[Docs]


"""
{
            "externalId": {
                "kpHD": null,
                "imdb": "tt0466671",
                "_id": "636221a408cbd3f0377a2949"
            },
            "logo": {
                "_id": "62f00e510f5be41246db358e",
                "url": null
            },
            "poster": null,
            "rating": {
                "_id": "6339b882c22d011bb5ea8647",
                "kp": 0,
                "imdb": 0,
                "filmCritics": 0,
                "russianFilmCritics": 0,
                "await": 0
            },
            "votes": {
                "_id": "6339b882c22d011bb5ea8648",
                "kp": 0,
                "imdb": 0,
                "filmCritics": 0,
                "russianFilmCritics": 0,
                "await": 0
            },
            "watchability": {
                "_id": "6339b882c22d011bb5ea8669",
                "items": null
            },
            "movieLength": null,
            "id": 118374,
            "type": "movie",
            "name": null,
            "description": null,
            "year": 1990,
            "alternativeName": "Ama... Bakit mo ako pinabayaan?",
            "enName": null,
            "names": [
                {
                    "_id": "6339b882c22d011bb5ea8646",
                    "name": "Ama... Bakit mo ako pinabayaan?"
                }
            ],
            "shortDescription": null,
            "releaseYears": []
        }


"""