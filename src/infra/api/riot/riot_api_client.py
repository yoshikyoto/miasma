# -*- coding: utf-8 -*-
import requests

class RiotApiClient(object):

    def __init__(self):
        self.base_url = "https://jp.api.pvp.net"

    def get(self, path, params={}):
        url = self.base_url + path
        params["api_key"] = self.api_key
        return requests.get(url, params=params).json()
