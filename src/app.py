# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, jsonify
import sys
#rootディレクトリでgunicornした時に正しく動くようにする
sys.path.append('src')
sys.path.append('.')
from domain.champion import ChampionService
from domain.news import NewsService
from domain.item import ItemService

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/v1/champions.json")
def champions():
    service = ChampionService()
    return jsonify(service.champions_dict())

@app.route("/api/v1/items.json")
def items():
    service = ItemService()
    return jsonify(service.items_dict())

@app.route("/api/v1/news.json")
def news():
    service = NewsService()
    print service.get_news_dict()
    return jsonify(service.get_news_dict())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, debug=True)
