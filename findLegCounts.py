#Problem Explanation
#A farmer asks you for help in telling the number of legs of all his animals. The farmer has three types of animals:
#chicken, cow, sheep *Respectively
#The farmer counted his animals and gave you a subtotal of all species. You need to implement a function that returns the total number of legs of all animals.

def hayvanlar(t, i, k):
    tavukBacak = 2*t
    inekBacak = 4*i
    koyunBacak = 4*k
    return tavukBacak + inekBacak + koyunBacak
