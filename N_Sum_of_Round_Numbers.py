import sys

def get_round_numbers(n):
    result = []
    factor = 1  # Start with 1 (unit place)
    
    while n > 0:
        digit = n % 10  # Extract last digit
        if digit > 0:
            result.append(digit * factor)  # Create a round number
        n //= 10  # Remove last digit
        factor *= 10  # Increase place value (1 → 10 → 100 …)
    
    return result

# Fast input reading
t = int(sys.stdin.readline().strip())  # Read number of test cases
output = []

for _ in range(t):
    n = int(sys.stdin.readline().strip())  # Read test case
    round_numbers = get_round_numbers(n)
    output.append(f"{len(round_numbers)}\n{' '.join(map(str, round_numbers))}")

# Efficient bulk printing
sys.stdout.write("\n".join(output) + "\n")
