print('Напишите предложение:')
string = input()
f = {}
for i in string:
    f[i] = f.get(i, 0) + 1
print(f)
