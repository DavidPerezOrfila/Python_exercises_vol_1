# Exercise 33
"""
The following variable is given:
num = 34
Using the appropriate method for an object of type str, print the variable num preceded by four zeros to the console as shown below.
Expected result:
000034
"""
num = 34
str_num = str(num)
result = str_num.zfill(6)
print(result)
