# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from champion_repository import ChampionRepository

class ChampionService(object):

    def __init__(self):
        self.__repository = ChampionRepository()

    def champions_dict(self):
        """
        apiで返せるdict形式でチャンピオンデータ一覧を取得
        """
        champions = self.__repository.champions()
        result = []
        for champion in champions:
            result.append({
                "key": champion.get_key(),
                "id": champion.get_id(),
                "name": champion.get_name(),
                "icon_url": champion.get_icon_url(),
            });
        return {"data": result}

    def get_champions_with_id_key(self):
        champions = self.__repository.champions_from_cache()
        result = {}
        for champion in champions:
            result[champion.get_id()] = champion
        return result

if __name__ == "__main__":
    service = ChampionService()
    print service.champions_dict()
    print service.get_champions_with_id_key()
