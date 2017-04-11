# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient

class StatsApiClient(RiotApiClient):

    def __init__(self):
        super(StatsApiClient, self).__init__()
        self.base_url = "https://global.api.pvp.net"

    def ranked_stats_by_summoner_id(self, summoner_id):
        path = "/api/lol/jp/v1.3/stats/by-summoner/" + str(summoner_id) + "/ranked"
        response = super(StatsApiClient, self).get(path, {})
        return response

if __name__ == "__main__":
    api = StatsApiClient()
    response = api.ranked_stats_by_summoner_id(6172436)
    print response.keys()
