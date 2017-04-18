# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from infra.api.riot import GameApiClient
from domain.champion import ChampionService
from game import Game
from stats import Stats

class GameRepository(object):

    def __init__(self):
        self.__api = GameApiClient()
        self.__champion_service = ChampionService()

    def recent_by_summoner_id(self, summoner_id):
        response = self.__api.get_recent_by_summoner_id(summoner_id)
        games = [];
        for game_data in response["games"]:
            if not game_data["gameMode"] == "CLASSIC":
                continue;
            champion = self.__champion_service.get_champion_by_id(game_data["championId"])

            stats_data = game_data["stats"]

            # playerRoleはrankedじゃないとついていない？
            player_role = None
            if stats_data.has_key("playerRole"):
                player_role = stats_data["playerRole"]

            player_position = None
            if stats_data.has_key("playerPosition"):
                player_position = stats_data["playerPosition"]

            stats = Stats(
                game_data["level"],
                player_role,
                player_position)
            game = Game(
                game_data["gameId"],
                game_data["gameType"],
                game_data["gameMode"],
                game_data["subType"],
                game_data["teamId"],
                champion,
                stats)
            # if game.is_ranked_solo():
            games.append(game)

        return games

if __name__ == "__main__":
    repo = GameRepository()
    games = repo.recent_by_summoner_id(6312300)
    game = games[0]
    print game.get_id()
    print game.get_team_id()
    print game.get_champion().get_name()
    print game.get_stats().get_player_role()
    #games = repo.recent_by_summoner_id(6172436)
