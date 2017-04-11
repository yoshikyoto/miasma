# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from infra.api.riot import ItemApiClient
from infra.dao import ItemDao
from domain.image import ImageUrlFactory
from item import Item

class ItemRepository(object):

    def __init__(self):
        self.__api = ItemApiClient()
        self.__dao = ItemDao()
        self.__image_url_factory = ImageUrlFactory()

    def items_from_api(self):
        """
        DBのデータを使わずriot apiからアイテム一覧を取得
        """
        item_response = self.__api.items()
        items = []
        for key, value in item_response["data"].iteritems():
            item = self.create_item_from_api_data(value)
            if item != False:
                items.append(item)
        return items

    def create_item_from_api_data(self, data):
        if not data.has_key("name"):
            return False
        if not data.has_key("description"):
            return False
        if not data.has_key("image"):
            return False
        # data["sanitizedDescription"] というのもある
        return Item(
            data["id"],
            data["name"],
            data["description"],
            self.__image_url_factory.item_image_url(data["image"]["full"]))

    def store_cache(self, item):
        cache = self.__dao.select(item.get_id())
        if cache is not None:
            self.__dao.delete(item.get_id())
        self.__dao.insert(
            item.get_id(),
            item.get_name(),
            item.get_description_html(),
            item.get_icon_url())

    def item_by_id(self, id):
        data = self.__dao.select(id)
        return Item(
            data["id"],
            data["name"],
            data["description_html"],
            data["icon_url"])

    def items_from_cache(self):
        items = []
        data = self.__dao.select_all()
        if(len(data) < 1):
            return items
        for i in data:
            items.append(Item(
                i["id"],
                i["name"],
                i["description_html"],
                i["icon_url"]))
        return items
            

if __name__ == "__main__":
    repo = ItemRepository()
    items = repo.items_from_api()
    print items[0].get_name()
    print items[0].get_id()
    print items[0].get_description_html()
    print items[0].get_icon_url()
