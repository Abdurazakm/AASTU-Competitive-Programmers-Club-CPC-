t = int(input())
st = "codeforces"
for _ in range(t):
    s = input()
    count = 0
    for i in range(10):
        if s[i]!=st[i]:
            count = count + 1
    print(count)