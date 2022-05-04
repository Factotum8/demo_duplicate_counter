from http import HTTPStatus

import tornado
from tornado import web

from mypackages import peewee_models
from mypackages.heandlers.version1.abstract_handler import AppHandler


class DeletingPayloadHandler(AppHandler):
    """
    The endpoint provides `delete` operation for payload.
    """

    async def get(self, slug):
        key = slug
        try:
            payload = await self.dao.get(peewee_models.Payloads, key=key)
        except peewee_models.DoesNotExist:
            raise tornado.web.HTTPError(HTTPStatus.NOT_FOUND, log_message=f'object: {key} not found')

        await self.dao.delete(payload)
        self.set_status(HTTPStatus.OK)
        await self.finish()
