# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
sys.path.append('src') #heroku run での実行用
from domain.champion import ChampionRepository
from domain.item import ItemRepository

print "update champions"
champion_repository = ChampionRepository()
champions = champion_repository.champions_from_api()
for champion in champions:
    champion_repository.store_cache(champion)
    print "update champion data " + champion.get_key() + " " + champion.get_name()

print "update items"
item_repository = ItemRepository()
items = item_repository.items_from_api()
# print items
for item in items:
    item_repository.store_cache(item)
    print "update item data " + str(item.get_id()) + " " + item.get_name()

print "end"
