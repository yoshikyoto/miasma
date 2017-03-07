# -*- coding: utf-8 -*-
import requests
import json
from riot_api_client import RiotApiClient

class ChampionApiClient(RiotApiClient):

    def __init__(self, api_key):
        super(ChampionApiClient, self).__init__()
        self.path = "/api/lol/jp/v1.2/champion"
        self.api_key = api_key

    def champions(self):
        path = self.path
        return super(ChampionApiClient, self).get(path)
