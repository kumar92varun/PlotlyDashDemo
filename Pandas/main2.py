import numpy
import pandas

#Creating a NumPy array
print('Array is:')
array = numpy.random.randint(0, 100, 30)
print(array)
print('\n')

#Converting NumPy array into NumPy matrix
print('Matrix is:')
matrix = array.reshape(10,3)
print(matrix)
print('\n')

#Converting NumPy Matrix into Pandas DataFrame
print('DataFrame is:')
dataframe = pandas.DataFrame(data=matrix, columns=['First', 'Second', 'Third'])
print(dataframe)
print('\n')