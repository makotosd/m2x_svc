# -*- coding: utf-8 -*-
from m2x.client import M2XClient
from flask import Flask, jsonify, request
import requests
import json


app = Flask(__name__)


@app.route('/machinist', methods=['POST'])
def machinist_post():
    posted_json = request.get_json()
    temperature = posted_json['value']['temperature']
    humidity = posted_json['value']['humidity']

    api_key = "daf7bbb9f5955136"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    data = {
        "agent": "Lime",
        "metrics": [
            {
                "name": "temperature",
                "namespace": "Environment Sensor",
                "data_point": {
                    "value": temperature
                }
            },
            {
                "name": "humidity",
                "namespace": "Environment Sensor",
                "data_point": {
                    "value": humidity
                }
            }
        ]
    }

    response = requests.post('https://gw.machinist.iij.jp/endpoint', headers=headers, data=json.dumps(data))

    return jsonify(response.text)


@app.route('/m2x', methods=['POST'])
def post():
    posted_json = request.get_json()
    temperature = posted_json['value']['temperature']
    humidity = posted_json['value']['humidity']

    client = M2XClient(key='81faa53c80c0c084e797d706bc84be25')  # API-KEY
    device = client.device('7870230c081b7f4f678dde08bc7bcba7')  # DEVICE-ID
    stream_temperature = device.stream('temperature')
    stream_humidity = device.stream('humidity')

    response_temperature = stream_temperature.add_value(float(temperature))
    response_humidity = stream_humidity.add_value(float(humidity))

    response = {'temperature': response_temperature,
                'humidity': response_humidity}

    return jsonify(response)


@app.route('/m2x_temperature', methods=['GET'])
def get_temperature():
    client = M2XClient(key='81faa53c80c0c084e797d706bc84be25')  # API-KEY
    device = client.device('7870230c081b7f4f678dde08bc7bcba7')  # DEVICE-ID
    stream = device.stream('temperature')

    response = stream.values()

    return jsonify(response)


@app.route('/m2x_humidity', methods=['GET'])
def get_humdity():
    client = M2XClient(key='81faa53c80c0c084e797d706bc84be25')  # API-KEY
    device = client.device('7870230c081b7f4f678dde08bc7bcba7')  # DEVICE-ID
    stream = device.stream('temperature')

    response = stream.values()

    return jsonify(response)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)