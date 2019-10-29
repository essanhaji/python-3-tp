from pprint import pprint

santence = input("Enter your santence : \n")

words = santence.split(" ")
# pprint(words)

print("This santence has {} words.".format(len(words)))