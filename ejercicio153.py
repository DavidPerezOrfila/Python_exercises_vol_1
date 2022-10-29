# Exercise 153
"""
The following dictionary is given:
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
"""
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
result = {value:key for key, value in stocks.items()}
print(result)