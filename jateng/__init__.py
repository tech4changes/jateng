from flask import Flask
from flask_restful import Resource, abort, Api
import json

app = Flask(__name__)
api = Api(app, prefix='/api/v1')

data = json.load(open('data/csv/data.json'))


def dataKosong(data_id):
    if data_id not in data:
        abort(404, message="data {} doesn't exist".format(data_id))


class kaka(Resource):
    def get(self, data_id):
        dataKosong(data_id)
        return data[data_id]


api.add_resource(kaka, '/<data_id>')

if __name__ == '__main__':
    app.run(debug=True)
