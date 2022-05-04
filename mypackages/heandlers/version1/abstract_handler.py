import base64
from typing import Optional, Awaitable

from tornado.escape import json_encode
from tornado.web import RequestHandler


class AppHandler(RequestHandler):
    """
    The endpoint provides adding a payload.
    """
    database = None
    dao = None
    bad_request = json_encode(dict(error='bad request'))

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def initialize(self) -> None:
        self.database = self.settings['database']
        self.dao = self.settings['dao']


class KeyGeneratorMixin:
    """
    The class provides method for generating key for a key-value storage.
    """
    @staticmethod
    async def generation_key(parameters: dict) -> str:
        codec = 'utf-8'
        s = ''.join(f' {k}+{v} ' for k, v in parameters.items())
        return base64.b64encode(s.encode(codec)).decode(codec)
