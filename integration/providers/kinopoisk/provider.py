import random
from integration.providers.kinopoisk.client import KinoPoiskAsyncClient
from integration.providers.kinopoisk import schemas
import json

class KinoPoinskAsyncProvider:
    """Async provider for kinopoisk.ru."""
    def __init__(self):
        self.client = KinoPoiskAsyncClient()

    async def get_movies(self) -> schemas.MoviesResponse:
        page = random.randint(1, 94152)
        params={"page": page}
        response = await self.client.request(method='GET', url='/movie', params=params)
        return schemas.MoviesResponse.parse_obj(json.loads(response.content))
    

kino_poisk_provider = KinoPoinskAsyncProvider()