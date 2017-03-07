# -*- coding: utf-8 -*-

class Champion(object):

    def __init__(self, id, key, name):
        self.id = id
        self.key = key
        self.name = name

    def get_id(self):
        return self.id

    def get_key(self):
        return self.key

    def get_name(self):
        return self.name
