# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from item_repository import ItemRepository

class ItemService(object):

    def __init__(self):
        self.__repository = ItemRepository()

    def items_dict(self):
        """
        apiで返せるdict形式でアイテムデータ一覧を取得
        """
        items = self.__repository.items_from_cache()
        result = {}
        for item in items:
            result[item.get_id()] = {
                "id": item.get_id(),
                "name": item.get_name(),
                "description_html": item.get_description_html(),
                "icon_url": item.get_icon_url(),
            }
        return {"data": result}

if __name__ == "__main__":
    service = ItemService()
    print service.items_dict()
