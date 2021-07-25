score = []
x = int(input("students number:"))
a = 0
b = 0
print(x)
for i in range(x):
    y = int(input("students score:"))
    score.append(y)

    b = b+y


print(score)
print("average score", b/x)


for i in score:
    print(i)

for i in score:
    if i > a:
        a = i
print("highest score",a)
    


