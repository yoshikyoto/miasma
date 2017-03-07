# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient
from champion import Champion
from image import Image

class ChampionApiClient(RiotApiClient):

    def __init__(self):
        super(ChampionApiClient, self).__init__()
        self.base_url = "https://global.api.pvp.net"
        self.path = "/api/lol/static-data/jp/v1.2/champion"

    def champions(self, champ_data="all"):
        """
        チャンピオン一覧を取得し、champion.Champion オブジェクトを返します
        """
        path = self.path
        params = {"champData": champ_data}
        response = super(ChampionApiClient, self).get(self.path, params)
        data = response["data"]
        champions = []
        for key, info in data.items():
            img = Image(
                info["image"]["full"],
                info["image"]["w"],
                info["image"]["h"],
                info["image"]["group"])
            c = Champion(int(info["id"]), key, info["name"], img)
            champions.append(c)
        return champions


if __name__ == "__main__":
    api = ChampionApiClient()
    champions = api.champions()
    c = champions[0];
    print c.get_id()
    print c.get_key()
    print c.get_name()
    print c.get_image().get_filename()
