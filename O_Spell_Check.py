t = int(input())  # Read number of test cases

for _ in range(t):
    n = int(input())  # Length of string
    s = input().strip()  # Read the string

    if n != 5:  # Check if length is not 5
        print("NO")
        continue

    # Correct characters that must be present exactly once
    required = ['T', 'i', 'm', 'u', 'r']
    found = [0] * 5  # To track occurrences of each character

    for char in s:
        for i in range(5):
            if char == required[i]:
                found[i] += 1

    # If each character appears exactly once, it's a valid spelling
    if found == [1, 1, 1, 1, 1]:
        print("YES")
    else:
        print("NO")
