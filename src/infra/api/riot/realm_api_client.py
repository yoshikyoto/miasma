# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient
from realm import Realm

class RealmApiClient(RiotApiClient):

    def __init__(self):
        super(RealmApiClient, self).__init__()
        self.base_url = "https://global.api.pvp.net"
        self.path = "/api/lol/static-data/jp/v1.2/realm"

    def realm(self):
        response = super(RealmApiClient, self).get(self.path, {})
        return Realm(
            response["v"],
            response["cdn"],
            response["n"]["champion"])

if __name__ == "__main__":
    client = RealmApiClient()
    r = client.realm()
    print r.get_version()
    print r.get_cdn()
    print r.get_champion()
