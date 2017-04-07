# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient

class SummonerApiClient(RiotApiClient):

    def __init__(self):
        super(SummonerApiClient, self).__init__()
        self.base_url = "https://jp.api.pvp.net"

    def get_by_name(self, name):
        path = "/api/lol/jp/v1.4/summoner/by-name/" + name
        response = super(SummonerApiClient, self).get(path, {})
        return response

if __name__ == "__main__":
    api = SummonerApiClient()
    print api.get_by_name("うたかた")
