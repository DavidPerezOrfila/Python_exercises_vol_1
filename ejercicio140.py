# Exercise 140
"""
Consider the two-roll of the dice. Create the probability space (omega) and calculate the probability of getting a sum of squares higher or equal to 45. Use set comprehension. Round the result to two decimal places and print the result to the console as shown below.
Expected result:
Probability: 0.22
"""
omega = {(x, y) for x in range(1, 7) for y in range(1, 7)}
a = {(x, y) for x, y in omega if x**2 + y**2 >= 45}
prob = round(len(a) / len(omega), 2)
print(f'Probability: {prob}')
