# -*- coding: utf-8 -*-
import MySQLdb

import sys
sys.path.append('../../')
from config import config

class Dao(object):

    def __init__(self):
        self.host = config.DB_HOST
        self.db = config.DB_NAME
        self.user = config.DB_USER
        self.password = config.DB_PASSWORD

    def connect(self):
        return MySQLdb.connect(
            host=self.host,
            db=self.db,
            user=self.user,
            passwd=self.password)

    def cursor(self, connection):
        return connection.cursor(MySQLdb.cursors.DictCursor)
