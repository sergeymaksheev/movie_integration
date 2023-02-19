import httpx


class BaseHttpAsyncClient(httpx.AsyncClient):
    
    async def request(self, *args, **kwargs):
        print(f"Start request with args {args} and kwargs {kwargs}")
        resp = await super().request(*args, **kwargs)
        print(f"Finished request: code={resp.status_code}, response: {resp}")
        if resp.is_success:
            return resp
        raise BaseException(resp)