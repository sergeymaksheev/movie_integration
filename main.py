from fastapi import FastAPI
from integration.providers.kinopoisk.provider import kino_poisk_provider
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Find_movie'
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck")
async def healtcheck():
    return {"status": "OK"}


@app.get("/v1/get-random-movie")
async def get_random_movie():
    return await kino_poisk_provider.get_random()


@app.post("/watched_movie")
async def watched_movie():
    pass


