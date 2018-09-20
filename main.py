from flask import Flask
from flask_restful import Api, Resource, reqparse
import os
app = Flask("ryan")
api = Api(app)

class Mainapp(Resource):
    def get(self, url):
        parser = reqparse.RequestParser()
        parser.add_argument(url)
        args = parser.parse_args()
        try:
            os.system("wget " + args[url])
            name = args[url].split('/')[args[url].split('/').__len__() - 1]
            os.system("mega-put ./{} /".format(name))
            os.system("rm " + name)
            return "{0} has been complitly downloaded!".format(name) , 200
        except:
            return "Usage: /start/url?url= your url put it here", 379

class Index(Resource):
    def get(self):
        return "Usage: /start/url?url= your url put it here", 200

api.add_resource(Mainapp, '/start/<string:url>')
api.add_resource(Index, '/')
app.run(debug = True)