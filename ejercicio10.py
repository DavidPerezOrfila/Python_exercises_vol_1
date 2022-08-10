# Exercise 10
"""
Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console as shown below.
Expected result:
Geometric average of the given numbers: 4.05
"""

x1, x2, x3, x4 = 4, 3, 4.5, 5

geo = (x1 * x2 * x3 * x4)

mean = geo ** (1/4)
# .2f para formatear a dos decimales
print(f'Geometric average of the given numbers: {mean:.2f}')
