# Write a program to determine if a number, given on the command line, is prime.

#  1. How can you optimize this program?
#  2. Implement [The Sieve of Eratosthenes]
#  (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), 
#  one of the oldest algorithms known (ca. 200 BC).

def is_prime(num):
  if num > 1:
    for i in range(2, num//2):
      if (num % i) == 0:
        print(f"Number {num} is not a prime number.")
        break
    else:
      print(f"Number {num} is a prime!")

  else:
    print(f"Number {num} is not a prime number.")


num = input("Enter a number: ")
num = int(num)

is_prime(num)
