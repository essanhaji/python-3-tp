sec = input("donner les seco :")

sec = int(sec)

s = sec % 60
m = sec // 60
h = m // 60
m = m % 60

print(h, " : ", m, " : ", s)
