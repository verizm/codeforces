n = int(input(""))
s = input("")

group4 = 0
group3 = 0
group2 = 0
group1 = 0
for num in s:
    if num == '1':
        group1 += 1
    elif num == '2':
        group2 += 1
    elif num == '3':
        group3 += 1
    elif num == '4':
        group4 += 1

taksicounter = 0
taksicounter += group4 # количесво такси для 4групп
taksicounter += group3 # количество такси для 3 групп

group1 = max(group1 - group3, 0) # считаем количество единиц которые не будут добавлены к тройкам
group2divizion = group2 // 2
taksicounter += group2divizion
ost = group2 % 2
if ost == 1:
    taksicounter += 1
    group1 = max(group1 - 2, 0)

group1divizion = group1 // 4
taksicounter += group1divizion
ost1 = group1 % 4
if ost1 > 0:
    taksicounter += 1

print(taksicounter)
