# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from infra.api.riot import SummonerApiClient
import summoner_data

class SummonerRepository(object):

    def __init__(self):
        self.__api = SummonerApiClient()

    def get_id_by_name(self, name):
        api_response = self.__api.get_by_name(name)
        data =  api_response[name]
        return data["id"]

if __name__ == "__main__":
    repo = SummonerRepository()
    print repo.get_id_by_name(summoner_data.UTAKATA_SUMMONER_NAME)
