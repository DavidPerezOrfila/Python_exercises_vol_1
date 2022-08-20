# Exercise 66
"""
The following filename is given:
filename = '01012020_sales.xlsx'
Check if the file has the 'xlsx' extension. Print to the console 'YES' if true, 'NO' if false.
Expected result:
YES
"""
filename = '01012020_sales.xlsx'

result = 'YES' if filename.endswith('xlsx') else 'NO'
print(result)
