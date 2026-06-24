lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
print(f"Prime numbers between {lower} and {upper} are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break  # Factor found, not a prime number
        else:
            print(num, end=" ")
print() 
