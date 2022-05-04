#!/usr/bin/env python3
# coding=utf-8
"""
Pushing fixture to DB
"""
import json
import os
from distutils.util import strtobool

from dotenv import load_dotenv

from mypackages.peewee_models import DATABASE, get_postgresql_database, Payloads


load_dotenv()


def create_fixture():
    """
    Insert into DB and create fixture file
    """
    unique_payload = Payloads().create(key='IGxvZ2luK215X2xvZ2luICBwYXNzd29yZCtteV9wYXNzd29yZCA=',
                                       arguments=json.dumps({"login": "my_login", "password": "my_password"}),
                                       duplicate_count=0)
    duplicated_payload = Payloads().create(key='IGxvZ2luK3VzZXIgIHBhc3N3b3JkK3F3ZXJ0eSA=',
                                           arguments=json.dumps({"login": "user", "password": "qwerty"}),
                                           duplicate_count=2)

    # Dump fixture to file
    # with open('./fixture_tmp.json', 'w') as f:
    #     json.dump(dict(payloads=[Payloads().dump(unique_payload), Payloads().dump(duplicated_payload)]), f)


def main(config, with_fixture=False):
    """
    Init migration
    inset test data
    """
    database = get_postgresql_database(config)
    DATABASE.initialize(database)
    DATABASE.connect()
    DATABASE.create_tables([Payloads])
    if with_fixture:
        create_fixture()
    DATABASE.close()


if __name__ == '__main__':
    main(dict(os.environ), bool(strtobool(os.getenv('IS_IMPORTING_FIX'))))
