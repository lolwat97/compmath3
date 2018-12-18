from functools import reduce
from itertools import combinations
from operator import add
from operator import mul

class Calculator:
    def __init__(self):
        self.input = {}
        self.results = {}
        pass

    def set_input(self):
        pass

    def calculate(self):
        pass

    def print_results(self):
        for key, value in self.results.items():
            print('{}:\n{}'.format(key, value))
