from http import HTTPStatus
from json import JSONDecodeError

import tornado
from tornado import web
from tornado.escape import json_decode

from mypackages import peewee_models
from mypackages.heandlers.version1.abstract_handler import AppHandler, KeyGeneratorMixin
from mypackages.heandlers.version1.schemas.putting_payload import (PuttingPayloadRequestSchema,
                                                                   PuttingPayloadResponseSchema)


class PuttingPayloadHandler(AppHandler, KeyGeneratorMixin):
    """
    The endpoint provides `put` operation for payload.
    """

    async def post(self, slug):
        key = slug
        try:
            parameters = PuttingPayloadRequestSchema(**json_decode(self.request.body))
        except JSONDecodeError:
            raise tornado.web.HTTPError(HTTPStatus.BAD_REQUEST)

        try:
            payload = await self.dao.get(peewee_models.Payloads, key=key)
        except peewee_models.DoesNotExist:
            raise tornado.web.HTTPError(HTTPStatus.NOT_FOUND, log_message=f'object: {key} not found')

        payload.arguments = parameters.json()

        response = PuttingPayloadResponseSchema(key=key)
        return self.write(response.json())
