n = int(input(""))
current_count = 0
max_count = 0
for i in range(0, n):
    string = input("")
    a, b = string.split(" ")
    a, b = int(a), int(b)
    current_count -= a
    current_count += b
    max_count = max(max_count, current_count)
print(max_count)
