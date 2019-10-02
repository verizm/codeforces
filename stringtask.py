def create_word(string):
    if len(string) > 10:
        lenght = len(string)
        number = lenght - 2
        a = string[0]
        b = string[-1]
        new_word = a + str(number) + b
        return new_word
    elif len(string) <= 10:
        return string
    else:
        print("non letter")

num = int(input(""))
for i in range(0, num):
    string = input("")
    print(create_word(string))
