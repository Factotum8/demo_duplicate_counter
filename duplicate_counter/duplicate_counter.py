# coding=utf-8
"""
The main executable module
"""
import os
from typing import Optional, Awaitable

from dotenv import load_dotenv
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado_prometheus import PrometheusMixIn, MetricsHandler

from mypackages import peewee_models
from mypackages.heandlers.version1.adding_payload_handler import AddingPayloadHandler
from mypackages.heandlers.version1.deleting_payload_handler import DeletingPayloadHandler
from mypackages.heandlers.version1.getting_payload_handler import GettingPayloadHandler
from mypackages.heandlers.version1.putting_payload_handler import PuttingPayloadHandler

load_dotenv()


class MainHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.write("Hello, world")


class ServerCounter(PrometheusMixIn, Application):
    """
    Main class
    """


def make_app(config: dict):
    database = peewee_models.PeeweeRepositoryBuilder()(peewee_models, config)  # init db connect
    dao = peewee_models.Manager(database)  # init data access object

    return ServerCounter([
        (r"/metrics", MetricsHandler),
        (r"/", MainHandler),
        # TODO I prefer path `api/v1/some_endpoint`
        (r"/api/add", AddingPayloadHandler),
        (r"/api/get", GettingPayloadHandler),
        (r"/api/remove", DeletingPayloadHandler),
        (r"/api/update/([^/]+=$)", PuttingPayloadHandler),
    ],
        # can call by self.settings['database']
        database=database,
        dao=dao)


def main():
    manager_server = make_app(dict(os.environ))

    manager_server.listen(port=int(os.getenv('APPLICATION_LISTEN_PORT')), address=os.getenv('APPLICATION_LISTEN_HOST'))
    IOLoop.current().start()


if __name__ == '__main__':
    main()
