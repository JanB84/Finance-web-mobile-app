
import flask
from flask import Flask
from flask import request
from flask_api import status
from flask.views import MethodView
from flask import Flask, jsonify, request
import uuid

from flask import send_from_directory

import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

dummy_data = {
    '1': {'date': '15/11/2018', 'amount': '15.50', 'category': 'test', 'spender': 'mich', 'desc': 'this is the day that...'},
    '2': {'date': '16/11/2018', 'amount': '16.50', 'category': 'test2', 'spender': 'andreea', 'desc': 'this is the day that...'},
    '3': {'date': '17/11/2018', 'amount': '18.50', 'category': 'test3', 'spender': 'parents', 'desc': 'this is the day that...'},
    '4': {'date': '18/11/2018', 'amount': '-1.50', 'category': 'test4', 'spender': 'kids', 'desc': 'this is the day that...'}
}


@app.route('/', methods=['GET'])
def show_index_page():
    return send_from_directory('static', 'index.html')


class Transaction(MethodView):
    def get(self):
        return jsonify(dummy_data), 200

    def put(self):
        data = request.json
        try:
            assert data['date']
            assert data['amount']
            assert data['spender']
            assert data['type']
            assert data['category']
        except:
            return jsonify({'result': 'assertion error'}), 500
        dummy_data[str(uuid.uuid4())] = data
        return jsonify(data), 200

    def post(self):
        return jsonify({"test": "test"}), 200

tnx_view = Transaction.as_view('transation')
app.add_url_rule(
    '/transaction', view_func=tnx_view, methods=['POST', 'PUT', 'GET'],
    strict_slashes=False
)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)