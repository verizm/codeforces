n = int(input(""))
# list = [4, 7, 47, 74, 447, 474, 744, 774, 747, 477]
# for num in list:
#     r = n % num
#     if r == 0:
#         print("YES")
#         exit(0) # выход из программы
#
# print("NO")

for num in range(1, 1001):
    snum = str(num)
    counter = 0
    for char in snum:
        if char == "4" or char == "7":
            counter += 1
    if counter == len(snum):
        print(num)
