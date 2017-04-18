# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient

class MatchApiClient(RiotApiClient):

    def __init__(self):
        super(MatchApiClient, self).__init__()
        self.base_url = "https://jp.api.pvp.net"

    def match_list_by_summoner_id(self, summoner_id, begin_time=None):
        params = {}
        if not begin_time is None:
            params["beginTime"] = begin_time
        print params
        path = "/api/lol/jp/v2.2/matchlist/by-summoner/" + str(summoner_id)

        response = super(MatchApiClient, self).get(path, params)
        return response


if __name__ == "__main__":
    api = MatchApiClient()
    print api.match_list_by_summoner_id(6312300)
