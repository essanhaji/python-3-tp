import sys
from copy import copy

line = input()
formal = copy(line)
line = line.split()

if len(line) != 3:
    print("The format was wrong")
    sys.exit()
else:
    first = int(line[0])
    operation = line[1]
    second = int(line[2])

    val = 0

    if operation == '+':
        val = first + second
    elif operation == '-':
        val = first - second
    elif operation == '*':
        val = first * second
    elif operation == '/':
        if second == 0:
            print("Impossible to devise by zero ")
            sys.exit()
        else:
            val = first / second
    else:
        print("The operators is note true")

print("{line} = {val}".format(line=formal, val=val))
