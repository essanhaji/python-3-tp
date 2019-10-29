
n = int(input("Enter a number : "))
if n >= 2:
    divisors = []
    for index in range(2, n):
        if n % index == 0:
            print(index)
            divisors = divisors + [index]
    if len(divisors) > 0:
        print("The number {:} is not prime number because it divisible by {:}".format(n, divisors))
    else:
        print("The number {:} is an prime number".format(n))
else:
    print("The number {:} is note prime number".format(n))