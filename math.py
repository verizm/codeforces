string = input("")

string = string.replace("+", "")
one = string.count("1")
two = string.count("2")
three = string.count("3")
new_string = []

for i in range(0, one):
    new_string.append("1")
for x in range(0, two):
    new_string.append("2")
for x in range(0, three):
    new_string.append("3")

sort_string = "+".join(new_string)
print(sort_string)