# Exercise162
'''
Using the math built-in module, implement the function called sigmoid()
'''
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))
