#Write a python program and display all prime number within an interval
start = -14
end = 30

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1): #end + 1 to include end
    if num > 1: # all prime numbers greater than 1
        for i in range(2, num): #from 2 to num 
            if (num%2)==0: #if a number can divided to 2, it is not a prime number
                break # we break loop if it is not a prime number
        else:
            print(num)
