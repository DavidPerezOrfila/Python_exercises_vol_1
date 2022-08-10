# Calculate the future value of 1000 USD with an anual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent

current_value = 1000
rate = 0.03
period = 5

future_value = current_value * (1 + rate) ** period
print(f'The future value of the investment: {future_value:.2f} USD')
