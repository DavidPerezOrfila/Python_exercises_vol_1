# Exercise 147
"""
The present value - pv and the investment period - n are given below:
pv = 1000
n = 10
Depending on the interest rates given below, calculate the value of interest on
investments:
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
Round the result to the full cent and print the result to the console.
Expected result:
[104.62, 218.99, 343.92, 480.24, 628.89, 790.85, 967.15]
"""
PV = 1000
N = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
FVS = [round(PV * (1 + r) ** N, 2) for r in rate]
interest = [round(fv - PV, 2) for fv in FVS]
print(interest)
