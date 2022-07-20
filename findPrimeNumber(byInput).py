#find prime number for every input
number = int(input("Please write your number to find Prime Number or Not: "))
prime = True

if number <= 1:
    prime = False

for i in range(2, number):

    if (number%i)==0:
        prime = False
        break
    
if prime == True:
    print("Your number is a prime number")
else:
    print("Your number is not prime number")



    
