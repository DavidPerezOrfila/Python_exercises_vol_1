# Exercise 107
"""
The following variables are given:
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}
Using the appropriate function, check if the variables are instances of tuple class. Print the result to the console as shown below.
Tip: Use the isinstance() built-in function.
Expected result:
False
False
True
False
False
"""
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}
print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))
