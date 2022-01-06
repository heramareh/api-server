#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File   : music.py
# @Author : liwang
# @Time   : 2021-12-26 19:07
import json
import re
import time
import requests
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
        # path = request.args.get('path')
        path = "E:\\FrontendProject\\vuetest\\static"
        # path = "/home/liwang/FrontendProject/vuetest/static"
        for root, dir, files in os.walk(path):
            for id, file in enumerate(files, 1):
                datas.append({"id": id, "name": file, "src": './static/'+file})
        return jsonify({"code": 200, "data": datas})

class SearchMusic(Resource):

    def __search(self, song_name):
        """搜索歌曲"""
        search_url = "https://songsearch.kugou.com/song_search_v2?callback=jQuery112405132987859127838_{}&page" \
                     "=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_fil" \
                     "ter=0&_={}&keyword={}".format(str(int(time.time() * 1000)), str(int(time.time() * 1000)),
                                                    song_name)
        obj = requests.get(search_url)
        start = re.search("jQuery\d+_\d+\(?", obj.text)
        data = json.loads(obj.text.strip().lstrip(start.group()).rstrip(")"))
        return data['data']['lists']

    def __get_song(self, song_info):
        """下载歌曲"""
        # 展示前十个搜索结果
        print(str(song_info['FileName']).replace('<em>', '').replace('</em>', ''))
        file_hash = song_info['FileHash']
        album_id = song_info['AlbumID']
        url = "http://m.kugou.com/app/i/getSongInfo.php?cmd=playInfo&hash={}&album_id={}".format(file_hash, album_id)
        obj = requests.get(url)
        data = obj.json()  # json格式
        return data

    def get(self):
        datas = []
        id = 1
        name = request.args.get('name').strip()
        song_list = self.__search(name)
        if song_list:
            for song_info in self.__search(name)[:10]:
                song = self.__get_song(song_info)
                src = song['url']
                img = song['imgUrl'].replace("{size}", "260").replace("https", "http")
                if src:
                    datas.append({"id": id, "name": str(song_info['FileName']).replace('<em>', '').replace('</em>', ''), "src": src, "img": img})
                    id += 1
        return jsonify({"code": 200, "data": datas})

if __name__ == '__main__':
    pass