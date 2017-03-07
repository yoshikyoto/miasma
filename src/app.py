# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

port = int(os.environ.get("PORT", 80))
app.run(port=port)
