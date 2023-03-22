from integration.providers.kinopoisk.client import KinoPoiskAsyncClient
from integration.providers.kinopoisk import schemas
import json

class KinoPoinskAsyncProvider:
    """Async provider for kinopoisk.ru."""
    def __init__(self):
        self.client = KinoPoiskAsyncClient()


    # async def get_random_v1(self) -> schemas.MoviesResponse:
    #     page = random.randint(1, 94152)
    #     random_movie = random.randint(0,9)
    #     params={"page": page}
    #     response = await self.client.request(method='GET', url='/v1/movie', params=params)
    #     data = json.loads(response.content.decode("utf-8"))
    #     movie_lst =  schemas.MoviesResponse.parse_obj(data)
    #     result = movie_lst.docs[random_movie]
    #     return result
    

    async def get_random(self):
        response = await self.client.request(method='GET', url='/v1/movie/random', params=self.client.params)
        data = json.loads(response.content.decode("utf-8"))
        movie_lst =  schemas.MoviesResponse.parse_obj(data)
        # print(movie_lst)
        # result = movie_lst.doc
        return movie_lst

    async def push_movie_in_base(result):
        pass
    

kino_poisk_provider = KinoPoinskAsyncProvider()

kino_poisk_provider.get_random()