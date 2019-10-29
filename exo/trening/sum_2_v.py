

v1 = [x+2*x for x in range(10)]
print(v1)


for i in range(len(v1)-1):
    for J in range(len(v1)-1):
        if v1[i] < v1[i+1] :
            v1[i], v1[i+1] = v1[i+1], v1[i]
print(v1)