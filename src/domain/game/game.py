# -*- coding: utf-8 -*-

class Game(object):

    def __init__(self, id, team_id, champion, stats):
        self.__id = id
        self.__team_id = team_id
        self.__champion = champion
        self.__stats = stats

    def get_id(self):
        return self.__id

    def get_team_id(self):
        return self.__team_id

    def get_champion(self):
        return self.__champion

    def get_stats(self):
        return self.__stats
