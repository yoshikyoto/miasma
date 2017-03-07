# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return 'hello'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)
