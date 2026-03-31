N = int(input())
v = list((map(int, input().split())))
num = 0
lookingfor = int(input())
for i in v:
    if i == lookingfor:
        num += 1
print(num)