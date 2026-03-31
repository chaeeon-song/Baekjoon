N, M = map(int, input().split())
box = []
for x in range(N):
    box.append(x+1)
for t in range(M):
    i, j = map(int, input().split())
    box[i-1], box[j-1] = (box[j-1], box[i-1])
for a in box:
    print(a, end = " ")