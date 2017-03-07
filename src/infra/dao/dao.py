# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

import sys
sys.path.append('../../')
from config import config

class Dao(object):

    def __init__(self):
        self.host = config.DB_HOST
        self.db_name = config.DB_NAME
        self.user = config.DB_USER
        self.password = config.DB_PASSWORD

    def connect(self):
        return psycopg2.connect(
            "host=" + self.host +
            " dbname=" + self.db_name +
            " user=" + self.user +
            " password=" + self.password)

    def cursor(self, connection):
        return connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
