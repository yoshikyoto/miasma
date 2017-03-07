# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from domain.champion import ChampionRepository

repository = ChampionRepository()
champions = repository.champions_from_api()
for champion in champions:
    repository.store_cache(champion)
    print "update data " + champion.get_key() + " " + champion.get_name()
