string1 = input("")
string2 = input("")
if string1.lower() < string2.lower():
    print("-1")
elif string2.lower() < string1.lower():
    print("1")
else:
    print("0")

