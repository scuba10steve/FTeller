import json
import os.path

class Question(object):
    """docstring for Question"""
    def __init__(self, question, file):
        super(Question, self).__init__()
        self.question = question
        self.file = file

    def get_question(self, direction):
        return self.question

    def setChild(self, question):
        self.question = question

    def parse_file(self, filename):
        assert os.path.isfile(filename)
        self.file = open(filename, 'r')
        return str(self.file.read())
