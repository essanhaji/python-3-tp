from math import factorial as fact
# from math import abs

def not_pair_number_next(nbr):
    i = 2
    while(True):
        status = True
        nbr += 1
        for i in range(2, nbr):
            if nbr % i == 0:
                status = False
                break
        if status:
            print("X -> _{}_".format(nbr))
            return nbr


X = float(input("enter X : "))
N = int(input("enter N : "))

S1 = X
S2 = 0
eps = 0.0001
n = 2

for NN in range(N):
    num = not_pair_number_next(n)
    S2 = S1 + (pow(X, num) / fact(num))

    # print("==> {eps}".format(eps = abs(S1 - S2)))

    if abs(S1 - S2) <= eps:
        print("<> {eps}".format(eps = abs(S1 - S2)))
        break
    n = num
    S1 = S2
