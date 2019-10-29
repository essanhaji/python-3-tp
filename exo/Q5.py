
number = int(input("enter your number : "))

divisors = []

for i in range(1, number // 2):
    if number % i == 0:
        divisors += [i]

if sum(divisors) == number:
    # print(sum(divisors))
    print("The number {number} is a perfect number ".format(number = number))
else:
    print("The number {number} is Not a perfect number".format(number = number))