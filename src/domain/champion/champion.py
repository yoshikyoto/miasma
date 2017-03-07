# -*- coding: utf-8 -*-

class Champion(object):

    def __init__(self, id, key, name, icon_url, q, w, e, r):
        self.__id = id
        self.__key = key
        self.__name = name
        self.__icon_url = icon_url
        self.__q = q
        self.__w = w
        self.__e = e
        self.__r = r

    def get_id(self):
        return self.__id

    def get_key(self):
        return self.__key

    def get_name(self):
        return self.__name

    def get_icon_url(self):
        return self.__icon_url

    def get_q(self):
        return self.__q
