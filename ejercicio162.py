# Exercise162
'''
Using the math built-in module, implement the function called sigmoid()
'''
import math


def sigmoid(var_x):
    """_summary_

    Args:
        var_x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return 1 / (1 + math.exp(-var_x))
