# Exercise 154
"""The following dictionary is given:
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}"""
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
result = {key:val for key, val in stocks.items() if val > 100}
print(result)