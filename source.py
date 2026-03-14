# A Function that give Sum of given Integer
def sigma(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
# This will take value from User
n = int(input("Enter a Number: "))
# This will call the function
print(sigma(n))
