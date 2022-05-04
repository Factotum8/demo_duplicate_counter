# coding=utf-8
r"""
Example
=======

The module is models for ORM peewee-async.
There are 1 table:

+----------------------+
| Payloads
+======================+
| ``key``             |
+----------------------+
| ``arguments``             |
+----------------------+
| ``duplicate_count``         |
+----------------------+

"""
import peewee
import peewee_asyncext
from peewee_async import Manager
from peewee import PeeweeException, DoesNotExist
from playhouse.postgres_ext import JSONField

__all__ = ['PeeweeException', 'BaseRepositoryPeeweeException', 'PeeweeRepositoryBuilder', 'Manager', 'Payloads',
           'DoesNotExist', 'DATABASE', 'get_postgresql_database']

# This instruction is the correct way to dynamically defining a database
DATABASE = peewee.DatabaseProxy()


class BaseRepositoryPeeweeException(Exception):
    """
    Base exception for this repository
    """
    pass


class BaseModel(peewee.Model):
    """
    model definitions - the standard "pattern" is to define a base model class
    that specifies which database to use.  then, any subclasses will automatically
    use the correct storage.
    """

    class Meta:
        database = DATABASE  # closure


def get_postgresql_database(config: dict) -> peewee_asyncext.PostgresqlExtDatabase:
    """
    Init db obj and return
    """
    return peewee_asyncext.PostgresqlExtDatabase(
        config['PG_DB_NAME'],
        user=config['PG_DB_LOGIN'],
        password=config['PG_DB_PASS'],
        host=config['PG_DB_HOST'],
        port=config['PG_DB_PORT'],
    )


def init_postgresql_database(config: dict):
    DATABASE.initialize(get_postgresql_database(config))
    DATABASE.connect()
    return DATABASE


class Payloads(BaseModel):
    """
    Model for table pages
    """
    key = peewee.CharField(null=True,
                           db_column='key',
                           help_text='base64 key',
                           unique=True,
                           index=True, )
    arguments = JSONField(null=True,
                          db_column='kwargs',
                          help_text='key words argument', )
    duplicate_count = peewee.IntegerField(null=True,
                                          db_column='duplicates_count',
                                          help_text='Payloads count which duplicates this payload',
                                          default=0, )


class PeeweeRepositoryBuilder:
    """
    Create data access object
    """

    def __init__(self):
        self.module = None

    def __call__(self, module, config: dict):
        return self.create_repository(module, config)

    def __del__(self):
        try:
            self.module.close()
        except Exception:
            pass

    def create_repository(self, module, config: dict):
        """
        Create peewee connector
        :param module: peewee_models
        :param config:
        :return:
        """
        module.DATABASE.initialize(self.connect(module, config))
        module.DATABASE.connect()
        self.module = module
        return module.DATABASE

    @staticmethod
    def connect(module, config: dict) -> peewee.PostgresqlDatabase:
        return module.get_postgresql_database(config)


if __name__ == '__main__':
    pass
