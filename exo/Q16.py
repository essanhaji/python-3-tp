
string = input("\nEnter your string : ")

string_inversed = string[::-1]

if string == string_inversed:
    print("Your string is mirorable")
else:
    print("Your string is NOT mirorable")