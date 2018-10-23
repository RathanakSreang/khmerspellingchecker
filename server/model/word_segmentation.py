#!/usr/bin/python
# -*- coding: utf-8 -*-

import model.trie as trie
from codecs import open, decode

class WordSegmentation:
  # init Trie class
  def __init__(self, text):
    self.text = text
    self.model = trie.Trie()
    self.model.load_from_pickle("train_data")
    self.result_all = []
    self.startIndex = 0

  def isNumber(self, ch):
    # number letter
    return ch in "0123456789០១២៣៤៥៦៧៨៩"

  def parseNumber(self, index):
    result = ""
    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch
      if self.isNumber(ch):
        result += self.text[index]
        index += 1
      else:
        return result

    return result
  def isEnglish(self, ch):
    return ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def parseEnglish(self, index):
    result = ""
    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch
      if (self.isEnglish(ch) or self.isNumber(ch)):
        result += ch;
        index += 1
      else:
        return result
    return result

  def get_suggestion(self, text):
    return "suggest word"

  def check_words(self):
    while(self.startIndex < len(self.text)):
      ch = self.text[self.startIndex]
      ch = ch.encode('utf-8')
      word = ''

      if self.isNumber(ch):
        word = self.parseNumber(self.startIndex).encode('utf-8')
      elif self.isEnglish(ch):
        word = self.parseEnglish(self.startIndex).encode('utf-8')
      else:
        word = self.parseTrie(self.startIndex)

      length = len(word.decode('utf-8'))
      result = {}
      if length == 0:
        result["text"] = ch.decode('utf-8')
        result["is_word"] = False
        self.result_all.append(result)
        self.startIndex += 1
        continue

      if self.model.searchWord(word) or self.isNumber(ch) or self.isEnglish(ch):
        result["text"] = word.decode('utf-8').encode('utf-8')
        result["is_word"] = True
      else:
        result["text"] = word.decode('utf-8').encode('utf-8')
        result["is_word"] = False
        result["suggest_word"] = self.get_suggestion(word.decode('utf-8'))

      self.result_all.append(result)
      self.startIndex += length

  def get_result(self):
    return self.result_all
