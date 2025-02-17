a, b, c = map(int, input().split())

count = 1  

if b != a:
    count += 1

if c != a and c != b:
    count += 1

print(count)
