import json
import os.path

file = None

class Question(object):
    """docstring for Question"""
    def __init__(self, question):
        super(Question, self).__init__()
        self.question = question

    def get_question(self, direction):
        return self.question

    def setChild(self, question):
        self.question = question

    def parse_file(self, filename):
        assert os.path.isfile(filename)
        global file = open(filename, 'r')
        return str(file.read())
