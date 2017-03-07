# -*- coding: utf-8 -*-

class Realm(object):

    def __init__(self, version, cdn, champion):
        self.version = version
        self.cdn = cdn
        self.champion = champion


    def get_version(self):
        return self.version

    def get_cdn(self):
        return self.cdn

    def get_champion(self):
        return self.champion
