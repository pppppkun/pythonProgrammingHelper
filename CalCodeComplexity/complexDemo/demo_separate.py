def countDif(num):
    if num > 50:
        return 1
    else:
        return -1


dif = 0
for i in range(50):
    for j in range(25):
        for k in range(15):
            dif += countDif(i+j+k)
print(dif)
