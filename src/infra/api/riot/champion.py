# -*- coding: utf-8 -*-

class Champion(object):

    def __init__(self, id, key, name, image):
        self.id = id
        self.key = key
        self.name = name
        self.image = image

    def get_id(self):
        """
        チャンピオンのID (int) を返します
        """
        return self.id

    def get_key(self):
        """
        チャンピオンのkey (string) を返します
        """
        return self.key

    def get_name(self):
        """
        チャンピオンの名前を返します
        """
        return self.name

    def get_image(self):
        """
        image.Image オブジェクトを返します
        """
        return self.image
