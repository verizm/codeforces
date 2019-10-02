a = "0000000"
b = "1111111"

string = input("")


if a in string:
    print("YES")
elif b in string:
    print("YES")
elif a and b in string:
    print("YES")
else:
    print("NO")