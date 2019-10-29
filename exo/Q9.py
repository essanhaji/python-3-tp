
A = int(input("Enter A : "))

u0 = 1
eps = 0.00000000000001

while True:
    un = (u0 + A / u0) / 2
    if abs(un**2 - A) < eps:
        print("Racine carre de {A} = {un}".format(A  = A, un = un))
        break
    u0 = un

