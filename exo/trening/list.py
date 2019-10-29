names = ["elhoucine", "21", "rayan", "-54", "mohamed", "adam"]
numbers = [1, 54, -55, 59, 21]

# print(names)
# print(names[0])
# del names[0]
#
# print(names)
# print(names[0])

names = names + ["Sanhoj", "hello"]
names.append("world")
print(names)
index = names.index("rayan")
#print("index : ", str(index))
names.sort()


names = ".".join(names)
print(names)

print("the min :", min(numbers))
print("the max :", max(numbers))
print("the len :", len(numbers))
print("the sum :", sum(numbers))

#print(names)

#names = "helloworld"
print("the min :", min(names))
print("the max :", max(names))
print("the len :", len(names))
#print("the sum :", sum(names))
