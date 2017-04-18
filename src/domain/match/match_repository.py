# -*- coding: utf-8 -*-
import sys
sys.path.append("../../")
from datetime import datetime, timedelta
from infra.api.riot import MatchApiClient

class MatchRepository(object):

    def __init__(self):
        self.__api = MatchApiClient()

    def matchids_by_summoner_id(self, summoner_id):
        # 2週間分データ取得すれば十分やろ
        two_weeks_ago = datetime.now() - timedelta(weeks=2)
        begin_timestamp_sec = int(two_weeks_ago.strftime('%s'))
        begin_timestamp_msec = begin_timestamp_sec * 1000

        response = self.__api.match_list_by_summoner_id(summoner_id, begin_timestamp_msec)
        match_references = response["matches"]
        ids = []
        for match_reference in match_references:
            # とりあえずRanked soloだけ
            print match_reference["timestamp"]
            if match_reference["queue"] == "RANKED_SOLO_5x5":
                ids.append(match_reference["matchId"])
        return ids


if __name__ == "__main__":
    repo = MatchRepository()
    ids = repo.matchids_by_summoner_id(6312300)
