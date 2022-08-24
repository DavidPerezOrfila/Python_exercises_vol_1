# Exercise 99
"""
Read the currencies.txt file. Each line has a different currency pair.
Create a list with the names of currency pairs containing the 'USD' symbol.
Expected result:
['ARSUSD', 'AUDUSD']
"""
with open('currencies.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

result = [i for i in lines if 'USD' in i]
print(result)
