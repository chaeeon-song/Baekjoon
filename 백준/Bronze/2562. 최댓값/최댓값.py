L = []
for x in range(9):
    number = int(input())
    L.append(number)
M = max(L)
print(M)
print(L.index(M)+1)