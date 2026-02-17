x = 1221
x = str(x)
array = []
for i in range(len(str(x))):
    # print("index: ", i, "value: ", x[i])
    array.append(x[i])

print(array)

array2 = []
for i in x[::-1]:
    print(i)
    array2.append(i)

print(array2)

print(array==array2)
    