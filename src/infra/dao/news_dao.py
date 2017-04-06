# -*- coding: utf-8 -*-

import sys
sys.path.append('../../')
from config import news_config

class NewsDao(object):

    def get_news(self):
        return news_config.news

if __name__ == "__main__":
    dao = NewsDao()
    print dao.get_news()
