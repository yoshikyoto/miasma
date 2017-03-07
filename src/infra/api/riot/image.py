# -*- coding: utf-8 -*-

class Image(object):

    def __init__(self, filename, width, height, group):
        self.filename = filename
        self.width = width
        self.height = height
        self.group = group

    def get_filename(self):
        return self.filename

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_group(self):
        return self.group
        
