
n = int(input("Enter N : "))

u0 = 0
print(" U0 = {}".format(u0))
u1 = 1
print(" U1 = {}".format(u1))

for i in range(2, n):
    un = u0 + u1
    print(" U{} = {}".format(i, un))
    u0 = u1
    u1 = un