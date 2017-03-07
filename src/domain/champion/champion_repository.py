# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import sys
sys.path.append('../../')
from infra.api.riot import ChampionApiClient
from infra.dao import ChampionDao
from domain.image import ImageUrlFactory
from domain.skill import Skill
from champion import Champion

class ChampionRepository(object):

    def __init__(self):
        self.__champion_api = ChampionApiClient()
        self.__image_url_factory = ImageUrlFactory()
        self.__dao = ChampionDao()

    def champions_from_api(self):
        """
        DBのキャッシュを使わず、riot apiからチャンピオン一覧を取得
        """
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
        infra.api.riot.Spell から domain.spell.Spell を生成
        """
        icon_url = self.__image_url_factory.skill_image_url(spell.get_image().get_filename())
        return Skill(
            spell.get_key(),
            spell.get_name(),
            icon_url)

    def __is_expired(self, created_at):
        """
        dbにキャッシュが生成されたのが6時間以上前かどうかを判定
        """
        delta = datetime.now() - created_at
        return delta > timedelta(hours=6)

    def champions_from_cache(self):
        """
        dbのキャッシュからチャンピオン一覧を取得
        キャッシュが古い場合は空配列がかえる
        """
        champions = []
        data = self.__dao.select_all()
        if(len(data) < 1):
            return champions
        if(self.__is_expired(data[0]["created_at"])):
            return champions
        for c in data:
            champions.append(Champion(
                c["id"],
                c["key"],
                c["name"],
                c["icon_url"],
                None,
                None,
                None,
                None))
        return champions

    def champions(self):
        """
        チャンピオン一覧を取得し
        必要があればキャッシュに乗せる
        """
        champions = self.champions_from_cache()
        if(len(champions) < 1):
            champions = self.champions_from_api()
            for champion in champions:
                self.store_cache(champion)
        return champions

    def store_cache(self, champion):
        """
        apiから取得したデータなどをキャッシュ(DB)に書き込む
        """
        cache = self.__dao.select(champion.get_key())
        if cache is not None:
            self.__dao.delete(champion.get_key())
        self.__dao.insert(
            champion.get_id(),
            champion.get_key(),
            champion.get_name(),
            champion.get_icon_url())

if __name__ == "__main__":
    repository = ChampionRepository()
    champs = repository.champions_from_api()
    print champs[2].get_q().get_icon_url()
    repository.champions_from_cache()
