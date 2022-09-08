# Exercise 138
"""
Consider the two-roll of the dice. Create the probability space (omega) and count the probability of getting a sum of points higher than 10. Use set comprehension.
Expected result:
Probability: 0.08
"""
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
print(f'Probability: {len(sum_gt_10) / len(omega):.2f}')
