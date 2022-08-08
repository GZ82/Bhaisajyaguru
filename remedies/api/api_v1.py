#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""api Bhaisajyaguru

Created on Aug 02 2022
@author: Zhen

"""
import os
import logging
from remedies.config import LOG_PATH
# <<< save to project folder
log_file_name = LOG_PATH + 'api_v1.log'
with open(log_file_name, 'w'):
    pass
logging.basicConfig(level=logging.DEBUG, filename=log_file_name, format='%(asctime)s %(levelname)s:%(message)s')

import sys
import shutil
import os
import pkg_resources
# import copy
# import numpy as np
import json
import itertools
import pickle
from PIL import Image

from flask import Flask, Response, jsonify, render_template_string, render_template, make_response, send_file, after_this_request, session
from flask_restful import reqparse, abort, Api, Resource

# def encoded_image(pil_img):
#     # pil_img: PIL file from drawer, functions for APIs
#     byte_arr = io.BytesIO()
#     pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
#     encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
#     return encoded_img
    

# class NumpyEncoder(json.JSONEncoder):
#     # convert np.array to json
#     def default(self, obj):
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return json.JSONEncoder.default(self, obj)

# def load_v_info(v_info_json):
#     # v_info_json: args['v_info']
#     # return: v_info, a nested array
#     v_info = json.loads(v_info_json)
#     v_info = np.asarray(v_info[1])
#     colnames = np.array([['ID','smi']])
#     v_info = np.array([colnames, v_info], dtype = object)
#     return v_info


# set up api
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
IMAGE_FOLDER = os.path.join('resources', 'images')
SOUND_FOLDER = os.path.join('resources', 'sounds')
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER 
app.config['SOUND_FOLDER'] = SOUND_FOLDER 
api = Api(app)

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response


#####################
# home
#####################
# load the main Pictures of Bhaisajyaguru
# @app.route('/api/v1/api_v1/home', methods=['GET'])
# def short_router_welcome():
#     filename = pkg_resources.resource_filename('remedies', 'resources/images/main_pic.jpeg')
#     return send_file(filename, mimetype='image/jpg')

# parser = reqparse.RequestParser()
@app.route("/home")
def home():
    img_path = os.path.join(app.config['IMAGE_FOLDER'], 'main_pic.jpg')
    return render_template('home.html', image=img_path)

# background sound
@app.route("/wav")
def streamwav():
    def generate():
        sound_bk = os.path.join(app.config['SOUND_FOLDER'], 'bk_sound.wav')
        with open(sound_bk, "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

#@app.route("/ogg")
#def streamogg():
#    def generate():
#        with open("signals/song.ogg", "rb") as fogg:
#            data = fogg.read(1024)
#            while data:
#                yield data
#                data = fogg.read(1024)
#    return Response(generate(), mimetype="audio/ogg")

#####################
# login logout
#####################
#https://realpython.com/using-flask-login-for-user-management-with-flask/

@app.route('/api/v1/api_v1/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        session['user'] = user
        return redirect(url_for('searh_round_first'))
    else:
        if 'user' in session:
            return redirect(url_for('searh_round_first'))
        return redirect(url_for('login'))
#     filename = pkg_resources.resource_filename('chemrouter', 'resources/CDI logo_final_sm.jpg')
#     return send_file(filename, mimetype='image/jpg')
@app.route('/api/v1/api_v1/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
  
if __name__ == '__main__':
    # 
    app.run(host='0.0.0.0', port=3000, debug=True)

