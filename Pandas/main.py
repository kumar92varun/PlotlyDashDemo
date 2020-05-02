import pandas as pd

data = pd.read_csv('details.csv')

#Printing whole data
print('Printing whole data:')
print(data)
print('\n')

#Printing only 1 column
print('Printing only Age column:')
print(data['Age'])
print('\n')

#Printing a few selected columns
print('Printing Age and Name columns:')
print(data[['Age', 'Name']])
print('\n')

#Printing minimum value of a column
print('Printing minimum Age:')
print(data['Age'].min())
print('\n')

#Printing maximum value of a column
print('Printing maximum Age:')
print(data['Age'].max())
print('\n')

#Printing mean value of a column
print('Printing mean Age:')
print(data['Age'].mean())
print('\n')