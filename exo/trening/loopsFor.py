numbers = [10, 23, 13, 5, 87, 21]

print(10 in numbers)

for index in range(len(numbers)):
    # print(index)
    # print(str(index) + " = ", numbers[index])
    print("the index {:d} = {:d}".format(index, numbers[index]))
