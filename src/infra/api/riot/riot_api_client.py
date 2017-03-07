# -*- coding: utf-8 -*-
import requests

import sys
sys.path.append('../../../')
from config import config

class RiotApiClient(object):

    def __init__(self):
        self.api_key = config.RIOT_API_KEY


    def get(self, path, params):
        url = self.base_url + path
        params["api_key"] = self.api_key
        return requests.get(url, params=params).json()
