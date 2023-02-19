from fastapi import FastAPI
from integration.providers.kinopoisk.provider import kino_poisk_provider

app = FastAPI(
    title='Find_movie'
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/healthcheck")
async def healtcheck():
    return {"status": "OK"}


@app.get("/get-random-movie")
async def get_random_movie():
    res = await kino_poisk_provider.get_movies()
    return res.json()



