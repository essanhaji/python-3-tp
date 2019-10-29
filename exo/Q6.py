

def number_perfect(number):

    divisors = []

    for i in range(1, number // 2):
        if number % i == 0:
            divisors += [i]

    if sum(divisors) == number:
        # print(sum(divisors))
        # print("The number {number} is a perfect number ".format(number = number))
        return True
    else:
        # print("The number {number} is Not a perfect number".format(number = number))
        return False


number = int(input("enter your number : "))

# print(number_perfect(number))

for i in range(1, number + 1):
    if number_perfect(i):
        print("The number {i} is a perfect number ".format(i = i))