n = int(input(""))
sum_x = 0
sum_y = 0
sum_z = 0
for i in range(0, n):
    string = input("")
    x, y, z = string.split(" ")
    x, y, z = int(x), int(y), int(z)
    sum_x += x
    sum_y += y
    sum_z += z

if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")