
firstName = str(input("enter your first name :"))
middleName = str(input("enter your middle name :"))
lastName = str(input("enter your last name :"))

firstName = firstName.capitalize()
middleName = middleName.capitalize()
lastName = lastName.capitalize()

fullName = "{first} {middle:.1s} {last}"

print(fullName.format(first=firstName, middle=middleName, last=lastName))
