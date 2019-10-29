import numpy as np
from pprint import pprint

try:
    print("\nTo make the production of the two matrices defind it need to have the dimention in this format n*m and m*h .\n")

    print("---------------------------------------")

    lenght_matrice_1_n = int(input("Enter the n of the first matrice : "))
    lenght_matrice_1_m = int(input("Enter the m of the secound matrice : "))
    matrice_1 = np.random.randint(10, size=(lenght_matrice_1_n, lenght_matrice_1_m))
    pprint(matrice_1)

    print("\n---------------------------------------")

    lenght_matrice_2_n = int(input("Enter the n of the first matrice : "))
    lenght_matrice_2_m = int(input("Enter the m of the secound matrice : "))
    matrice_2 = np.random.randint(10, size=(lenght_matrice_2_n, lenght_matrice_2_m))
    pprint(matrice_2)

    print("\n---------------------------------------")

    if lenght_matrice_1_m == lenght_matrice_2_n :
        result = np.random.randint(1, size=(lenght_matrice_1_n, lenght_matrice_2_m))

        for i in range(lenght_matrice_1_n):
            for j in range(lenght_matrice_2_m):
                for k in range(lenght_matrice_1_m):
                    # lenght_matrice_2_n and lenght_matrice_2_n has the samme value
                    result[i][j] += matrice_1[i][k] * matrice_2[k][j]
        pprint(result)
    else:
        print("The product of the two matrice is not defined !!!!!")
except Exception as erorr:
    print("Ops !!!")
    print(erorr)
finally:
    print("\n---------------------------------------")
    print("Thank (❁◡❁) you for using my program\n")

    
