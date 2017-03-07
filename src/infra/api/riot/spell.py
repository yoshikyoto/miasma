# -*- coding: utf-8 -*-

class Spell(object):

    def __init__(self, key, name, image):
        self.__key = key
        self.__name = name
        self.__image = image

    def get_key(self):
        return self.__key

    def get_name(self):
        return self.__name

    def get_image(self):
        return self.__image
