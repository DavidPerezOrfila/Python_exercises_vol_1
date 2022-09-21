# Exercise 141
"""
Consider a three-roll of the dice. Create the probability space (omega) and
calculate the probability of obtaining three values which the sum is divisible
by 7. Use set comprehension. Round the result to two decimal places and print
the result to the console as shown below.
Expected result:
Probability: 0.14
"""
omega = {(x, y, z) for x in range(1, 7)
         for y in range(1, 7) for z in range(1, 7)}
a = {(x, y, z) for x, y, z in omega if (x + y + z) % 7 == 0}
prob = round(len(a) / len(omega), 2)
print(f'Probability: {prob}')
