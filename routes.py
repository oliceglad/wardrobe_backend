from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from parser.parsewb import ParseWB


app = Flask(__name__)
CORS(app)
api = Api(app)

get_goods = ParseWB.get_category

class WbGoods(Resource):
    def get(self):
        category = request.args.get('category')
        return {'data': get_goods(category)}

api.add_resource(WbGoods, '/goods')

if __name__ == '__main__':
    app.run(debug=True)