students = []
for x in range(30):
    students.append(x+1)
for y in range(28):
    attended = int(input())
    if attended in students:
        a = students.index(attended)
        students.pop(a)
for z in students:
    print(z)