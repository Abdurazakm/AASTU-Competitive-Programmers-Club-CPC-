t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if a + b == c:
        print("YES")
    elif a + c == b:
        print("YES")
    elif b + c == a:
        print("YES")
    else:
        print("NO")
