mylist = []
x = int(input("students number:"))

b = 0
print(x)
for i in range(x):
    y = int(input("students score:"))
    mylist.append(y)

    b = b+y
print(mylist)
print(b/x)

