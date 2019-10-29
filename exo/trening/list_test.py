
# string = "6202562056056002198618901110056605646540646150180"

# print(string.count("0"))

# my_list = []
# my_list = string.split("0")

# print(my_list)

def sum_vecteur(v1, v2):
    if len(v1) == len(v2):
        return[ v1[i] + v2[i] for i in range(len(v1))]
    else :
        return False

print(sum_vecteur([1, 2, 3], [1, 2, 3]))