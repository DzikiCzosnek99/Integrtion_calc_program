from math import *
import numpy as np


class Integration:
    def __init__(self, func, lower_limit, upper_limit, time_step=None):
        self.func = func
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.time_step = time_step
        if self.time_step is None:
            i = abs(self.upper_limit - self.lower_limit)
            r = len(str(floor(i)))
            self.time_step = (i/100**r)

    def return_func(self, x):
        copy = self.func
        copy = copy.replace('x', str(x))
        copy = copy.replace('^', '**')
        return eval(copy)

    def calculation(self,h):
        result = self.return_func(self.lower_limit) + self.return_func(self.upper_limit)
        x = self.lower_limit = h
        while x < self.upper_limit:
            result = result + 2 * self.return_func(x)
            x = round(x+h,12)
        result = result * 0.5 * h
        return result
    def results(self):
        return self.calculation(h=self.time_step) + (1 / 3) * (self.calculation(h=self.time_step) - self.calculation(h=2 * self.time_step))




