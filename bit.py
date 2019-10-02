n = int(input())
x = 0
for string in range(0, n):
    iter = input("")
    if iter[1] == "+":
        x += 1
    else:
        x -= 1
print(x)