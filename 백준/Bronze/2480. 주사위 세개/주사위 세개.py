A, B, C = map(int, input().split())
if A == B == C :
    print(f'{10000+A*1000}')
elif A == B : #A == B or A == C 로 묶어줬으면 한 줄 줄일 수 있었음.
    print(f'{1000+A*100}')
elif B == C :
    print(f'{1000+B*100}')
elif C == A :
    print(f'{1000+C*100}')
else :
    print(max(A, B, C)*100) #max() 함수 기억하자!!