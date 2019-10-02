

def count_task(list):
    counter = []
    for element in list:
        element = element.replace(" ", "")
        element = element.count('1')
        counter.append(element)
    return counter


num = int(input(""))
list = []
for i in range(0, num):
    string = input("")
    list.append(string)

counter = count_task(list)
answer = 0
for i in counter:
    if i >= 2:
        answer +=1
print(answer)


