# -*- coding: utf-8 -*-

class Skill(object):

    def __init__(self, key, name, icon_url):
        self.__key = key
        self.__name = name
        self.__icon_url = icon_url

    def get_key(self):
        return self.__key

    def get_name(self):
        return self.__name

    def get_icon_url(self):
        return self.__icon_url
