# -*- coding: utf-8 -*-

class Champion(object):

    def __init__(self, id, key, name, image, spells):
        self.__id = id
        self.__key = key
        self.__name = name
        self.__image = image
        self.__spells = spells

    def get_id(self):
        """
        チャンピオンのID (int) を返します
        """
        return self.__id

    def get_key(self):
        """
        チャンピオンのkey (string) を返します
        """
        return self.__key

    def get_name(self):
        """
        チャンピオンの名前を返します
        """
        return self.__name

    def get_image(self):
        """
        image.Image オブジェクトを返します
        """
        return self.__image

    def get_spells(self):
        return self.__spells

    def get_spell(self, index):
        return self.__spells[index]
