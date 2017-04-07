# -*- coding: utf-8 -*-
from riot_api_client import RiotApiClient

class ItemApiClient(RiotApiClient):

    def __init__(self):
        super(ItemApiClient, self).__init__()
        self.base_url = "https://global.api.pvp.net"
        self.path = "/api/lol/static-data/jp/v1.2/item"

    def items(self, item_list_data="all"):
        params = {"itemListData": item_list_data}
        response = super(ItemApiClient, self).get(self.path, params)
        return response

if __name__ == "__main__":
    api = ItemApiClient()
    print api.items()
