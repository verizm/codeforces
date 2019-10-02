string = input("")
n, k = string.split(" ")
n, k = int(n), int(k)

line = input("")
ratings = line.split(" ")

index_k = int(ratings[k- 1])

i = 0
for element in ratings:
    if int(element) >= index_k and int(element) > 0:
        i +=1
print(i)
