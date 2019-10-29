from pprint import pprint

def distinct_characters(string):
    alphabet = set()
    for i in range(len(string)):
        alphabet.add(string[i])
    return alphabet

print("\n---------------------------------------")

our_string = input("Enter your String :\n")
alphabet = distinct_characters(our_string)

print("\n---------------------------------------")

count_distinct_characters_sorted = []

for item in alphabet:
    count_distinct_characters_sorted.append((item, our_string.count(item)))
    print(" The count of '{}' is {}".format(item, our_string.count(item)))

# pprint(count_distinct_characters_sorted)
# count_distinct_characters_sorted = sorted(count_distinct_characters_sorted)
# pprint(count_distinct_characters_sorted)
