# -*- coding: utf-8 -*-
import requests

class RiotApiClient(object):

    def __init__(self):
        self.base_url = "https://jp.api.pvp.net"

    def get(self, path):
        url = self.base_url + path
        print "get " + url
        return requests.get(url).json()
