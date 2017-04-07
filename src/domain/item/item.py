# -*- coding: utf-8 -*-

class Item(object):

    def __init__(self, id, name, description_html, icon_url):
        self.__id = id
        self.__name = name
        self.__description_html = description_html
        self.__icon_url = icon_url

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_description_html(self):
        return self.__description_html

    def get_icon_url(self):
        return self.__icon_url
