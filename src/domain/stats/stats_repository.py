# -*- coding: utf-8 -*-
import sys
sys.path.append("../../")
from infra.api.riot import StatsApiClient
from domain.champion import ChampionService

class StatsRepository(object):

    def __init__(self):
        self.__api = StatsApiClient()
        self.__champion_service = ChampionService()

    def get_ranked_stats_by_summoner_id(self, summoner_id):
        api_response = self.__api.ranked_stats_by_summoner_id(summoner_id)
        if not api_response.has_key("champions"):
            return []
        champions_cache = self.__champion_service.get_champions_with_id_key()
        for champion_stats_data in api_response["champions"]:
            champion_id = champion_stats_data["id"]
            # idが0のこともあるのでその場合はskip
            # https://developer.riotgames.com/api-methods/#stats-v1.3/GET_getRankedStats
            if not champions_cache.has_key(champion_id):
                continue
            champion = champions_cache[champion_id]
            print champion.get_name()


if __name__ == "__main__":
    repo = StatsRepository()
    repo.get_ranked_stats_by_summoner_id(6312300)
