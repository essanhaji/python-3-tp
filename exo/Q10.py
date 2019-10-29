import numpy as np

# N = int(input("Enter N : "))

# vec = np.random.uniform(size=(N, 1))  # a 3x3x3 array
# print(vec)

print("--------------------------------------------------------")

# from -100 to 100 generate 10 values


# vec = np.linspace(-100.0, 100.0, 10)

vec = [-100.0, -77.77777778, -55.55555556, -33.33333333, -11.11111111, 11.11111111, 33.33333333, 55.55555556, 1.258, 100.0, ]

print(vec)

for i in range(len(vec)):
    if type(vec[i]) == "None":
        print(" => Is empty")
else:
    print(" => This vectors doesn't have any empty value")

