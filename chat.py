s = input("")

hello = "hello"
i = -1
try:
    for char in hello:
        i = s.index(char, i + 1)

    print('YES')
except:
    print('NO')
