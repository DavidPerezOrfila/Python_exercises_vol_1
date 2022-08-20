# Exercise 70
"""
The following password is given:
password = 'cskdnjcasa#!'
Check if the password has at least 11 characters and contains the special character '!'.
If so, print 'Password correct', otherwise 'Password incorrect'.
Expected result:
Password correct
"""
password = 'cskdnjcasa#!'
print('Password correct' if len(password) >=
      11 and '!' in password else 'Password incorrect')
