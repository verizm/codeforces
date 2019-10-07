from collections import defaultdict

string = input("")

# dictionary = {}
# for s in string:
#    count = string.count(s)
#    dictionary[s] = count

dictionary = {}
for s in string:
    if dictionary.get(s) == None:
        dictionary.setdefault(s, 0)
    dictionary[s] += 1

counter = len(dictionary.keys())
if counter % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
