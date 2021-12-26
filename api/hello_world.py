#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : hello_world.py
# @Author : liwang
# @Time   : 2021-12-26 15:59
from flask_restful import Resource
from flask import jsonify

class HelloWorld(Resource):
    def get(self):
        return jsonify({"code": 200, "data": [
        {"id":1, "name":"少年", "author":"梦然", "src":"./static/少年-梦然.mp3"},
        {"id":2, "name":"微微", "author":"傅如乔", "src":"./static/微微-傅如乔.mp3"},
        {"id":3, "name":"世界这么大还是遇见你", "author":"程响", "src":"./static/世界这么大还是遇见你-程响.mp3"},
        {"id":4, "name":"桥边姑娘", "author":"海伦", "src":"./static/桥边姑娘-海伦.mp3"},
    ]})

if __name__ == '__main__':
    pass