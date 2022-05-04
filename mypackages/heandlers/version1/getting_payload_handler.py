from http import HTTPStatus

import tornado
from tornado import web
from tornado.escape import json_decode

from mypackages import peewee_models
from mypackages.heandlers.version1.abstract_handler import AppHandler
from mypackages.heandlers.version1.schemas.getting_payload import GettingPayloadRequestSchema


class GettingPayloadHandler(AppHandler):
    """
    The endpoint provides `get` operation for payload.
    """

    async def get(self):
        key = self.get_argument('key')
        try:
            payload = await self.dao.get(peewee_models.Payloads, key=key)
        except peewee_models.DoesNotExist:
            raise tornado.web.HTTPError(HTTPStatus.NOT_FOUND)

        response = GettingPayloadRequestSchema.parse_obj({**json_decode(payload.arguments),
                                                          'duplicates': payload.duplicate_count})
        return self.write(response.json())
