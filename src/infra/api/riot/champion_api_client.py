# -*- coding: utf-8 -*-
import json
import ConfigParser
from riot_api_client import RiotApiClient
from champion import Champion

import sys
sys.path.append('../../../')
from config import config

class ChampionApiClient(RiotApiClient):

    def __init__(self):
        super(ChampionApiClient, self).__init__()
        self.path = "/api/lol/jp/v1.2/champion"
        self.api_key = config.RIOT_API_KEY

    def champions(self):
        path = self.path
        response = super(ChampionApiClient, self).get(path)
        champions = []
        for champion_response in response["champions"]:
            c = Champion(champion_response["id"])
            champions.append(c)
        return champions

if __name__ == "__main__":
    api = ChampionApiClient()
    print api.champions()
