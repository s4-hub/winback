# import os, shelve, markdown

# from flask import Flask, g

# # create an instance of Flask
# app = Flask(__name__)

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = shelve.open("db.sqlite3")
#     return db

# @app.teardown_appcontext
# def teardown_db(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# @app.route("/api/json")
# def index():
    
#     with open('datas.json', 'r') as f:
#         content = f.read()

#     return markdown.markdown(content)