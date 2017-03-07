# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from domain.champion import ChampionRepository

class ChampionService(object):

    def __init__(self):
        self.__repository = ChampionRepository()

    def champions_dict(self):
        champions = self.__repository.champions_from_cache()
        result = []
        for champion in champions:
            result.append({
                "name": champion.get_name(),
                "icon_url": champion.get_icon_url(),
            });
        return {"data": result}

if __name__ == "__main__":
    service = ChampionService()
    print service.champions_dict()
