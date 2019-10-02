def create_string(string):
    string = string.lower()
    simbols = ['a', 'o', 'y', 'e', 'u', 'i']
    for element in simbols:
        string = string.replace(element, "")
    string = '.'.join(string)
    return "." + string

string = input()
print(create_string(string))
