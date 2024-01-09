#A code to test if a given number is prime or not
def IsPrime(n):
    #corner cases
    if n <= 1:
        return False
    #non prime numbers from 2 to n-1
    for i in range(2, n):
        n % i == 0
        return False
    else:
        return True
    
IsPrime(int(input("What number do you want to check if it is prime or not?")))
if IsPrime:
    print("This number is a prime number!")
else:
    print("This number is not a prime number")