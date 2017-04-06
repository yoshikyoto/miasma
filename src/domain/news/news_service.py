# -*- coding: utf-8 -*-

import sys
sys.path.append('../../')
from infra.dao import NewsDao

class NewsService(object):

    def __init__(self):
        self.__dao = NewsDao()

    def get_news_api_response(self):
        return self.__dao.get_news()

if __name__ == "__main__":
    service = NewsService()
    print service.get_news_api_response()
