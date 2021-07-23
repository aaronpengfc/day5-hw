score = []

x = int(input("students number:"))

b = 0
print(x)
for i in range(x):
    y = int(input("students score:"))
    score.append(y)

    b = b+y
print(score)
print(b/x)
for i in score:
    print(i)