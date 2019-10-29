import numpy as np
from pprint import pprint


N1 = int(input("Enter the value of N1 : "))
N2 = int(input("Enter the value of N2 : "))

vec1 = np.linspace(-100.0, 100.0, N1)
vec2 = np.linspace(-100.0, 100.0, N2)
vec3 = []

print("\n==>> vec1 ")
pprint(vec1)
print("\n==>> vec2 ")
pprint(vec2)

lenght = 0

if len(vec1) >= len(vec2) : 
    lenght = len(vec2)
    # print(lenght)
else:
    lenght = len(vec1)
    # print(lenght)

for i in range(lenght):
    vec3 +=  [vec1[i] +  vec2[i]]

print("\n==>> vec3 ")
pprint(vec3)
print("\n==>>",len(vec3))