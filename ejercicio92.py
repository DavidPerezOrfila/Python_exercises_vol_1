# Exercise 92
"""
Using the while loop, calculate how many years you have to wait for the return on the investment described below to at least double your money (we only take into account full periods).
Description:
n - number of periods (in years)
pv - present value
r - interest rate (annual)
fv - future value
Investment parameters:
pv = 1000
r = 0.04
Print result to the console as shown below.
Expected result:
Future value: 2025.82 USD. Number of periods: 18 years
"""
n = 1
pv = 1000
r = 0.04
value = pv * (1 + r)

while value <= pv * 2:
    value *= (1+r)
    n += 1
print(f'Future value: {value:.2f} USD. Number of periods: {n} years')
