#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from flask import Flask
from flask_restful import Resource, Api
from resources.home import Home
from resources.spelling_checker import SpellingCheck

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(SpellingCheck, '/sentences_checking')

if __name__ == '__main__':
  reload(sys)
  sys.setdefaultencoding('utf-8')
  app.run(debug=True)
