# -*- coding: utf-8 -*-
import json
import ConfigParser
from riot_api_client import RiotApiClient
from champion import Champion

class ChampionApiClient(RiotApiClient):

    def __init__(self):
        super(ChampionApiClient, self).__init__()
        self.base_url = "https://global.api.pvp.net"
        self.path = "/api/lol/static-data/jp/v1.2/champion"

    def champions(self, champ_data="all"):
        path = self.path
        params = {"champData": champ_data}
        response = super(ChampionApiClient, self).get(path, params)
        data = response["data"]
        champions = []
        for key, info in data.items():
            c = Champion(int(info["id"]), key, info["name"])
            champions.append(c)
        return champions

    
if __name__ == "__main__":
    api = ChampionApiClient()
    champions = api.champions()
    for champ in champions:
        print champ.get_name()
