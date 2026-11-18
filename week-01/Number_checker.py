num = int(input("Enter a number: "))

# Check Even or Odd
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Check Prime
if num <= 1:
    print(f"{num} is Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print(f"{num} is Prime" if is_prime else f"{num} is Not Prime")