# -*- coding: utf-8 -*-
from m2x.client import M2XClient
from flask import Flask, jsonify, request


app = Flask(__name__)


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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)