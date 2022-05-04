from http import HTTPStatus
from json import JSONDecodeError

import tornado
from tornado import web
from tornado.escape import json_decode

from mypackages import peewee_models
from mypackages.heandlers.version1.abstract_handler import AppHandler, KeyGeneratorMixin
from mypackages.heandlers.version1.schemas.adding_payload import AddingPayloadResponseSchema, AddingPayloadRequestSchema


class AddingPayloadHandler(AppHandler, KeyGeneratorMixin):
    """
    The endpoint provides adding a payload.
    """

    async def post(self):
        try:
            parameters = AddingPayloadRequestSchema(**json_decode(self.request.body))
        except JSONDecodeError:
            raise tornado.web.HTTPError(
                HTTPStatus.BAD_REQUEST,
                log_message=f"payload isn't valid: {self.request.body.decode('utf-8', errors='ignore')}"
            )

        key = await AddingPayloadHandler.generation_key(parameters.dict())

        try:
            payload = await self.dao.get(peewee_models.Payloads, key=key)
            payload.duplicate_count += 1
            await self.dao.update(payload)
        except peewee_models.DoesNotExist:
            # A payload appears first time
            payload = peewee_models.Payloads().create(key=key,
                                                      arguments=parameters.json(),
                                                      duplicate_count=0)
            payload.save()

        response = AddingPayloadResponseSchema(key=key)
        return self.write(response.json())
