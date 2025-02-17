t = int(input())  
for _ in range(t):  
    ticket  = input() 
    first_three_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    last_three_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if first_three_sum == last_three_sum:
        print("YES")
    else:
        print("NO")
        