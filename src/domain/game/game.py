# -*- coding: utf-8 -*-

class Game(object):

    def __init__(self,
                 id,
                 game_type,
                 game_mode,
                 sub_type,
                 team_id,
                 champion,
                 stats):
        self.__id = id
        self.__game_type = game_type
        self.__game_mode = game_mode
        self.__sub_type = sub_type
        self.__team_id = team_id
        self.__champion = champion
        self.__stats = stats

    def get_id(self):
        return self.__id

    def get_game_type(self):
        return self.__game_type

    def get_game_mode(self):
        """
        "CLASSIC": クラシック
        """
        return self.__game_mode

    def get_sub_type(self):
        """
        "NORMAL": ノーマル
        "RANKED_SOLO_5x5": ソロランク
        """
        return self.__sub_type

    def is_ranked_solo(self):
        return self.__sub_type == "RANKED_SOLO_5x5"

    def get_team_id(self):
        return self.__team_id

    def get_champion(self):
        return self.__champion

    def get_stats(self):
        return self.__stats
