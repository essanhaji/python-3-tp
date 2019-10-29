import math
from math import sqrt

print(" ax² + bx + c = 0")

a = input("donner la valeur de a :")
b = input("donner la valeur de b :")
c = input("donner la valeur de c :")

a, b, c = int(a), int(b), int(c)

Del = b ** 2 - 4 * a * c

print(" Del = ", Del)

if Del < 0:
    print("\npas de soulution reel")
elif Del == 0:
    print("\nLa soulution de cette Equoition :")
    x = -b / (2 * a)
    print("\n x = ", x)
else:
    print("\nLes deux soulution des cette Equoition :")
    x1 = (-b + sqrt(Del)) / (2 * a)
    print("\n X1 = ", x1)
    x2 = (-b - sqrt(Del)) / (2 * a)
    print("\n X2 = ", x2)
print("\n")
