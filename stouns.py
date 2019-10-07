n = int(input(""))
s = input("")
size = 0
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        size += 1
print(size)