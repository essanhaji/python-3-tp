def reversString(word):
    return word[::-1]


def palindrome(word):
    if word == word[::-1]:
        print("The word '{:}' is a palindrome".format(word))
        pass
    else:
        print("The world '{:}' is note a palindrome".format(word))


string = "hello world"
print("The string '{:}' = '{:}'".format(string, reversString(string)))

palindrome("abbbba")
palindrome("helleh")
palindrome("meee")
palindrome("no way")

