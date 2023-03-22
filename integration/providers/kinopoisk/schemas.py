"""Kinopoisk response schemas."""
from typing import List
from pydantic import BaseModel



# class Names(BaseModel):
#     """Names schema"""
#     _id: str
#     name: str


# class Votes(BaseModel):
#     """Votes schema"""
#     kp: int
#     imdb: int
#     filmCritics: int
#     russianFilmCritics: int


# class Rating(BaseModel):
#     """Rating schema"""
#     kp: float
#     imdb: float
#     filmCritics: float
#     russianFilmCritics: float


# class Docs(BaseModel):
#     """Docs schema"""
#     rating: Rating
#     votes: Votes
#     movieLength: int | None
#     id: int
#     type: str
#     name: str | None
#     description: str | None
#     year: int | None
#     alternativeName: str | None
#     enName: str | None
#     names: list[Names]
#     shortDescription: str | None


# class MoviesResponse(BaseModel):
#     """Movies response schema"""
    
#     docs: list[Docs]
#     doc: Docs


class Names(BaseModel):
    """Names schema"""
    name: str

class Persons(BaseModel):
    """Persons schema"""
    id: int
    photo: str | None
    name: str | None
    enName: str | None
    profession: str | None
    enProfession: str | None

class Countries(BaseModel):
    """Countries schema"""
    name: str | None

class Genres(BaseModel):
    name: str | None

class Poster(BaseModel):
    url: str | None
    previewUrl: str | None

class Premiere(BaseModel):
    country: str | None
    world: str | None

class SpokenLanguages(BaseModel):
    name: str | None
    nameEn: str | None

class ProductionCompanies(BaseModel):
    name: str | None
    url: str | None
    previewUrl: str | None

class FramesCount(BaseModel):
    """FramesCount schema"""
    framesCount: int | None

class Votes(BaseModel):
    """Votes schema"""
    kp: int | None
    imdb: int | None
    filmCritics: int | None
    russianFilmCritics: int | None

class Rating(BaseModel):
    """Rating schema"""
    kp: float | None
    imdb: float | None
    filmCritics: float | None
    russianFilmCritics: float | None

class ExternalId(BaseModel):
    """ExternalId schema"""
    kpHD: str | None
    imdb: str | None
    tmdb: int | None

class Trailers(BaseModel):
    """Trailers schema"""
    url: str
    name: str
    site: str

class Videos(BaseModel):
    """Videos schema"""
    trailers: Trailers | None

class MoviesResponse(BaseModel):
    """Movies response schema"""
    #videos: list[Videos] | None
    status: str | None
    externalId: ExternalId | None
    rating: Rating | None
    votes: Votes | None
    movieLength: int | None
    images: FramesCount | None
    #productionCompanies: ProductionCompanies | None
    spokenLanguages: SpokenLanguages
    id: int
    type: str
    name: str | None
    description: str | None
    premiere: Premiere
    slogan: str | None
    year: int | None
    poster: Poster | None
    #facts: str | None
    genres: list[Genres]
    countries: list[Countries]
    persons: list[Persons]
    alternativeName: str | None
    enName: str | None
    names: list[Names]
    ageRating: int | None
    shortDescription: str | None
    top10: int | None
    top250: int | None
