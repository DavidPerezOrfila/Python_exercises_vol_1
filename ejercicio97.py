# Exercise 97
"""
The following dictionary is given:
users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
Try printing the value for the key:
user_id = '004'
In case of a KeyError, print to the console the following message:
'The 004 key is not in the dictionary. Adding key ...'
Then add this key to the dictionary with the value None and print the users dictionary to the console.
Expected result:
The 004 key is not in the dictionary. Adding key ...
{'001': 'Mark', '002': 'Monica', '003': 'Jacob', '004': None}
"""
users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'
try:
    print(users[user_id])
except KeyError:
    print(f'The {user_id} key is not in the dictionary. Adding key ...')
    users[user_id] = None
    print(users)
