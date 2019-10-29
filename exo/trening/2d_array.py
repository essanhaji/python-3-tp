
from pprint import pprint as pretty_print
from copy import copy, deepcopy

array1D = [1, 2, 3, 4, 5, 6]
array2D = [
    deepcopy(array1D),
    deepcopy(array1D),
    deepcopy(array1D)
]

print(array1D)
print("\n")
pretty_print(array2D)
array2D[1][1] = 8745
print(array1D)
pretty_print(array2D)
