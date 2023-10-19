"""
initialize the app

"""
# from flask import (
#     Blueprint, flash,g,redirect,render_template,
#     request,url_for)

# bp=Blueprint("blog",__name__)

import os

from flask import Flask


def create_app(test_config = None):
    """create and configure the app"""
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping
    (
        SECRET_KEY := "development",
        DATABASE := os.path.join(app.instance_path, "beige.sqlite3"),
    )

    if test_config:
        app.config.from_pyfile("config.py",silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except:
        pass

    @app.route("/hello")
    def hello():
        return "Hello World!!!"
    
    return app