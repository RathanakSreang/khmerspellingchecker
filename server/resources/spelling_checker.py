#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_restful import reqparse, Resource
import model.word_segmentation as word_segmentation

parser = reqparse.RequestParser()
parser.add_argument('sentences')

class SpellingCheck(Resource):
  def post(self):
    args = parser.parse_args()
    sentences = args['sentences']
    words = word_segmentation.WordSegmentation(sentences)
    words.check_words()
    return words.get_result(), 201
