t = int(input())
for _ in range(t):
    s = input()
    if s[0]=="Y" or s[0]=="y":
        if s[1]=="e" or s[1]=="E":
            if s[2] == "S" or s[2]=="s":
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")