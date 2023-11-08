k = 0
for i in range(1,20, 2):
    print(i, end=" ")
    if i != 19:
        print("+",end=" ")
    k += i
print(" = ",k)