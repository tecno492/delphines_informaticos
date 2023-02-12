dict = {'X': 0, 'E': 1, 'P': 2, 'O': 3, 'A': 4, 'W': 5, 'L': 6, 'C': 7, 'S': 8, 'R': 9}

def get_key(val):
    for key, value in dict.items():
        if val == value:
            return key

    return "key doesn't exist"

palabra1 = "SOLAR"
palabra2 = "POWER"
resultado = "EXCELS"
solu = [2, 0, 4, 8, 6, 3]

np1 = []
np2 = []

for a in palabra1:
    np1.append(dict[a])

ar = ""
for n in np1:
    ar += str(n)

np1 = int(ar)

for a in palabra2:
    np2.append(dict[a])

ar = ""
for n in np2:
    ar += str(n)

np2 = int(ar)

result = np1+np2

print(np1)
print(np2)
print(result)

s = ""
for n in solu:
    value = get_key(int(n))
    print(value)

#print(s)
