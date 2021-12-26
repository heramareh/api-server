#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : main.py
# @Author : liwang
# @Time   : 2021-12-26 15:57
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.hello_world import HelloWorld
from api.music import MusicList

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    api = Api(app)
    api.add_resource(HelloWorld, '/api/helloworld')
    api.add_resource(MusicList, '/api/musiclist')
    app.run(debug=True, port=8080)
