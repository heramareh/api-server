#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : music.py
# @Author : liwang
# @Time   : 2021-12-26 19:07
from flask_restful import Resource, request
from flask import jsonify
import os
# url参数，request.args.get('')
# form参数，request.form.get('')
# json参数，request.json['']
class MusicList(Resource):
    def get(self):
        datas = []
        # print(request.args.get('path'))
        for root, dir, files in os.walk(request.args.get('path')):
            for id, file in enumerate(files, 1):
                datas.append({"id": id, "name": file, "src": request.args.get('dir')+file})
        return jsonify({"code": 200, "data": datas})

if __name__ == '__main__':
    pass