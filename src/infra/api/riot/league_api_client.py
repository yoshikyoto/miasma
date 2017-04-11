# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient

class LeagueApiClient(RiotApiClient):

    def __init__(self):
        super(LeagueApiClient, self).__init__()
        self.base_url = "https://jp.api.pvp.net"

    def challenger(self, type):
        return self.get("challenger", type)

    def master(self, type):
        return self.get("master", type)

    def get(self, tier, type):
        path = "/api/lol/jp/v2.5/league/" + tier
        params = {"type": type}
        response = super(LeagueApiClient, self).get(path, params)
        return response


if __name__ == "__main__":
    api = LeagueApiClient()

    challenger = api.challenger("RANKED_SOLO_5x5")
    print challenger.keys()
    ce = challenger["entries"]
    print len(ce)
    for e in ce:
        print e["playerOrTeamName"]

    master = api.master("RANKED_SOLO_5x5")
    print master.keys()
    me = master["entries"]
    print len(me)
    for e in me:
        print e["playerOrTeamName"]
