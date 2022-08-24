# Exercise 2
"""
Calculate the future value of 1000 USD with an anual interest RATE of 3%,
annual capitalization and a 5-year investment PERIOD.
Round the result to the nearest cent
"""

CURRENT_VALUE = 1000
RATE = 0.03
PERIOD = 5

FUTURE_VALUE = CURRENT_VALUE * (1 + RATE) ** PERIOD
print(f'The future value of the investment: {FUTURE_VALUE:.2f} USD')
