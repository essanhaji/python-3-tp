import numpy as np
from pprint import pprint

try:
    print("---------------------------------------")

    lenght_of_vectors = int(input("\nEnter the lenght of the vectors : "))

    print("\n---------------------------------------\n")

    vector_1 = np.linspace(0.0, 50.0, lenght_of_vectors)

    print("==>> The first vector without sorting ")
    print(vector_1)

    vector_1 = sorted(vector_1)
    print("==>> The first vector sorted ASC ")
    print(vector_1)

    print("\n---------------------------------------")

    vector_2 = np.linspace(-100.0, 100.0, lenght_of_vectors)

    print("==>> The secound vector without sorting ")
    print(vector_2)

    vector_2 = sorted(vector_2)
    print("==>> The secound vector sorted ")
    print(vector_2)

    print("\n---------------------------------------")

    point_of_one_vector = 0
    point_of_secound_vector = 0
    for i in range(lenght_of_vectors):
        if vector_1[i] > vector_2[i]:
            point_of_one_vector += 1
            # print("-> {}".format(point_of_one_vector))
        elif vector_1[i] < vector_2[i]:
            point_of_secound_vector += 1
            # print("=> {}".format(point_of_secound_vector))

    if point_of_one_vector > point_of_secound_vector:
        print("The vector one is bigger than the secound vector '{}'".format(point_of_one_vector))
    else:
        print("The vector toos is bigger than the first vector '{}'".format(point_of_secound_vector))
except:
    print("errer !!")
