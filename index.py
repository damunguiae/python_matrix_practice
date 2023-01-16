import numpy as np

test_list = [1,2,3,4,5]
test_matrix = [test_list,test_list,test_list,test_list,test_list]
print(test_matrix)
# a matrix is like (elements, properties of elements) transposed - > (properties, all data for that property, for all elements)
matrix_np= np.array(test_matrix)

print(matrix_np.shape)
print(matrix_np)
