# Exercise158
"""
Using the built-in module for regular expressions, find all email addresses in
the following text:
raw_text = "Send an email to info@template.com or sales-info@template.it"
Print the result to the console.
Expected result:
['info@template.com', 'sales-info@template.it']
"""
import re

raw_text = "Send an email to info@template.com or sales-info@template.it"
result = re.findall(pattern=r"[\w\.-]+@[\w\.-]+", string=raw_text)
print(result)
