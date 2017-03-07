# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from infra.api.riot import RealmApiClient

class ImageUrlFactory(object):

    def __init__(self):
        self.__realm_api = RealmApiClient()
        self.__realm = None

    def __get_realm(self):
        """
        チャンピオンの画像を生成するたびにrealm apiを叩くのは効率が悪いので
        いい感じにキャッシュします
        """
        if self.__realm is None:
            self.__realm = self.__realm_api.realm()
        return self.__realm

    def champion_image_url(self, filename):
        realm = self.__get_realm()
        url = realm.get_cdn() + "/" + realm.get_champion() + "/img/champion/" + filename
        return url

    def skill_image_url(self, filename):
        realm = self.__get_realm()
        url = realm.get_cdn() + "/" + realm.get_version() + "/img/spell/" + filename
        return url


if __name__ == "__main__":
    factory = ImageUrlFactory()
    print "do it"
    # 1回目はAPIアクセスがあるので時間がかかるけど2回目は早いはず
    print factory.champion_image_url("Ahri.png")
    print factory.champion_image_url("Ahri.png")
    print factory.skill_image_url("AhriOrbofDeception.png")
    print factory.skill_image_url("AhriOrbofDeception.png")
