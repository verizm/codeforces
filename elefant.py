coord = int(input(""))
steps = [5, 4, 3, 2, 1]
counter = 0
for step in  steps:
    didvizion = coord // step
    counter += didvizion
    ost = coord % step
    coord = ost
print(counter)