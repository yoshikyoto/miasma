# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from infra.api.riot import SummonerApiClient
from infra.api.riot import LeagueApiClient
import summoner_data

class SummonerRepository(object):

    def __init__(self):
        self.__api = SummonerApiClient()
        self.__league_api = LeagueApiClient()

    def get_id_by_name(self, name):
        api_response = self.__api.get_by_name(name)
        data =  api_response[name]
        return data["id"]

    def get_challenger_ids(self):
        api_response = self.__league_api.challenger()
        ids = []
        for entry in api_response["entries"]:
            ids.append(int(entry["playerOrTeamId"]))
        return ids

if __name__ == "__main__":
    repo = SummonerRepository()
    print repo.get_id_by_name(summoner_data.UTAKATA_SUMMONER_NAME)
    print repo.get_challenger_ids()
