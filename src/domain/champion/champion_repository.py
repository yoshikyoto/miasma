# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from infra.api.riot import ChampionApiClient
from domain.image import ImageUrlFactory
from domain.skill import Skill
from champion import Champion

class ChampionRepository(object):

    def __init__(self):
        self.__champion_api = ChampionApiClient()
        self.__image_url_factory = ImageUrlFactory()

    def champions_from_api(self):
        champions = []
        champion_api_data = self.__champion_api.champions()
        for c in champion_api_data:
            champions.append(self.create_champion_from_api_champion(c))
        return champions

    def create_champion_from_api_champion(self, data):
        """
        infra.api.riot.Champion から domain.champion.Champion を生成
        """
        q = self.create_skill_from_api_spell(data.get_spell(0))
        w = self.create_skill_from_api_spell(data.get_spell(1))
        e = self.create_skill_from_api_spell(data.get_spell(2))
        r = self.create_skill_from_api_spell(data.get_spell(3))
        icon_url = self.__image_url_factory.champion_image_url(data.get_image().get_filename())
        return Champion(
            data.get_id(),
            data.get_key(),
            data.get_name(),
            icon_url,
            q,
            w,
            e,
            r)

    def create_skill_from_api_spell(self, spell):
        """
        imfra.api.riot.Spell から domain.spell.Spell を生成
        """
        icon_url = self.__image_url_factory.skill_image_url(spell.get_image().get_filename())
        return Skill(
            spell.get_key(),
            spell.get_name(),
            icon_url)

if __name__ == "__main__":
    repository = ChampionRepository()
    champs = repository.champions_from_api()
    print champs[2].get_q().get_icon_url()
