from flask import Flask, request
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

@api.route('/info')
class infoSimple(Resource):

    def get(self):
        return "Built with FlaskRESTplus"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
