t = int(input())  
for _ in range(t):  
    card = input()  
    if card == "abc":  
        print("YES")  
    elif card in ["acb", "bac", "cba"]:  
        print("YES")  
    else:  
        print("NO")  
