nums = input("")
n, t = nums.split(" ")
n, t = int(n), int(t)

s = input("")
ar = []
for char in s:
    ar.append(char)

for element in range(0, t):
    i = 0
    while i < n - 1:
        if ar[i] == 'B' and ar[i + 1] == 'G':
            ar[i] = 'G'
            ar[i + 1] = 'B'
            i += 2
        else:
            i += 1

string = ''.join(ar)
print(string)
