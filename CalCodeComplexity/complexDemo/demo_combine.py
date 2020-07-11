dif = 0
for i in range(50):
    for j in range(25):
        for k in range(15):
            if i + j + k > 50:
                dif += 1
            else:
                dif -= 1
print(dif)
