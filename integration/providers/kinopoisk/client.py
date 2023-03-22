from integration.base_client import BaseHttpAsyncClient


class KinoPoiskAsyncClient(BaseHttpAsyncClient):
    """Custom async http client for request to kinopoisk.ru."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url='https://api.kinopoisk.dev/'
        self.params = {"token": '1HSYQ5M-E8M4FA2-JD4012J-F6G72XS'}
        