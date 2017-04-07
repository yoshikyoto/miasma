# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient

class GameApiClient(RiotApiClient):

    def __init__(self):
        super(GameApiClient, self).__init__()
        self.base_url = "https://jp.api.pvp.net"

    def get_recent_by_summoner_id(self, summoner_id):
        """
        サモナーIDから直近の10ゲームを取得して返す
        """
        path = "/api/lol/jp/v1.3/game/by-summoner/" + str(summoner_id) + "/recent"
        response = super(GameApiClient, self).get(path, {})
        return response

if __name__ == "__main__":
    api = GameApiClient()
    print api.get_recent_by_summoner_id(6172436)
