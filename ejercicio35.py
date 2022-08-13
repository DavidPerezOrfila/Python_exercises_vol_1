# Exercise 35
"""
From the given url:
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
extract the slug after the last character '/'. Then replace all dashes with spaces and print the result to the console as shown below.
Expected result:
sciezka data scientist machine learning engineer
"""
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
url_as_list= url.split("/")
print(url_as_list[-1].replace("-", " "))
# Solution 2
name = url.split('/')[-1]
name = name.replace('-', ' ')
print(name)
