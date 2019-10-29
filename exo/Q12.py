
import numpy as np
from pprint import pprint

try:
    N = int(input("Enter the lenght of N : "))
    # type_sorte = input("Enter the way to sorte your vector (ASC or DESC) : ")

    vec = np.linspace(-100.0, 100.0, N)

    print("\n==>> The vector without sorting ")
    pprint(vec)

    vec = sorted(vec)
    print("\n==>> The vector sorted ASC ")
    pprint(vec)

    vec = sorted(vec, reverse=True)
    print("\n==>> The vector sorted DESC ")
    pprint(vec)
except:
    print("errer !!")
