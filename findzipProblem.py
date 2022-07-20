''' 
Problem Explanation:
Write a function that returns the index that goes "zip" a second time in a string, or -1 if it doesn't pass at least twice.

Examples:
zip("selam zip arıyorum zip ") ➞ 19
zip("merhaba zip arıyorum") ➞ -1
Uppercase "zip" is not the same as lowercase "zip".
To check your solution, use your function with 
print to say "This is the first zip and this is the second zip." 
Find the result of the expression. -> print(zip("This is the first zip and this is the second zip."))
'''

def zip(yazi):
    sayılan = yazi.count("zip")
    if sayılan < 2:
        return -1
    else:
        ilk = yazi.find("zip")
        return yazi.find("zip",ilk+1)
        
        
    
    
print(zip("Birinci zip bu iken ikinci zip budur."))
