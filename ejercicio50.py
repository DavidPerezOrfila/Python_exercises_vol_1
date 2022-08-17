# Exercise 50
"""
The following tuple is given:
Sort this tuple from a to z and print it to the console.
Tip: Tuples are immutable. You have to create a new one.
Expected result:
('aws', 'java', 'python', 'sql')
"""
techs = ('python', 'java', 'sql', 'aws')
sorted_techs = tuple(sorted(techs))
print(sorted_techs)
