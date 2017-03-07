# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient
from champion import Champion
from image import Image
from spell import Spell


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
        for champion_key, info in data.items():
            # スキル4つのparse
            spells = []
            for spell_info in info["spells"]:
                s = self.__parse_spell(spell_info)
                spells.append(s)

            # チャンピオンのparse
            champion_image = self.__parse_image(info["image"])
            c = Champion(
                int(info["id"]),
                champion_key,
                info["name"],
                champion_image,
                spells)
            champions.append(c)
        return champions

    def __parse_spell(self, spell_info):
        spell_image = self.__parse_image(spell_info["image"])
        return Spell(
            spell_info["key"],
            spell_info["name"],
            spell_image)

    def __parse_image(self, image_info):
        return Image(
            image_info["full"],
            image_info["w"],
            image_info["h"],
            image_info["group"])


if __name__ == "__main__":
    api = ChampionApiClient()
    champions = api.champions()
    c = champions[0];
    print c.get_id()
    print c.get_key()
    print c.get_name()
    print c.get_image().get_filename()
    print c.get_spell(0).get_name()
    print c.get_spell(1).get_key()
    print c.get_spell(2).get_image().get_filename()
