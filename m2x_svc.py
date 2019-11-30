# -*- coding: utf-8 -*-
from m2x.client import M2XClient
import json
from flask import Flask, jsonify
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    (t, h) = get_temperature()
    #(t, h) = get_temperature_dummy()
    dic = {
        'temperature': t,
        'humidity': h
    }
    dic2 = {
        'timestamp': datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'value': dic
    }
    return jsonify(dic2)



def get_from_m2x():
    client = M2XClient(key='81faa53c80c0c084e797d706bc84be25')  # API-KEY

    device = client.device('7870230c081b7f4f678dde08bc7bcba7')  # DEVICE-ID
    #  client.devices()
    device.stream("temperature").values(limit=6)

    # Get raw HTTP response
    raw = client.last_response.raw

    # Get HTTP respose status code (e.g. `200`)
    status = client.last_response.status

    # Get HTTP response headers
    headers = client.last_response.headers

    # Get json data returned in HTTP response
    res_json = client.last_response.json
    values = res_json['values']

    return values


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)