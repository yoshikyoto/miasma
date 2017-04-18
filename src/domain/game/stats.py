# -*- coding: utf-8 -*-

class Stats(object):

    def __init__(self, level, player_role, player_position):
        self.__level = level
        self.__player_role = player_role
        self.__player_position = player_position

    def get_player_role(self):
        """
        Player role (Legal values: DUO(1), SUPPORT(2), CARRY(3), SOLO(4))
        """
        return self.__player_role

    def get_player_position(self):
        """
        Player position (Legal values: TOP(1), MIDDLE(2), JUNGLE(3), BOT(4))
        """
        return self.__player_position
