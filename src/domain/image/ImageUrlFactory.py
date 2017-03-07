# -*- coding: utf-8 -*-

import sys
sys.path.append('../../')
from infra.api.riot import RealmApiClient

class ImageUrlFacotry(object):

    def __init__(self):
        self.realm_api = RealmApiClient()
        self.realm = None

    def __get_realm(self):
        """
        チャンピオンの画像を生成するたびにrealm apiを叩くのは効率が悪いので
        いい感じにキャッシュします
        """
        if self.realm is None:
            self.realm = self.realm_api.realm()
        return self.realm

    def champion_image_url(self, filename):
        realm = self.__get_realm()
        url = realm.get_cdn() + "/" + realm.get_champion() + "/img/champion/" + filename
        return url

if __name__ == "__main__":
    factory = ImageUrlFacotry()
    print "do it"
    # 1回目はAPIアクセスがあるので時間がかかるけど2回目は早いはず
    print factory.champion_image_url("Ahri.png")
    print factory.champion_image_url("Ahri.png")
