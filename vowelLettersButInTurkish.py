'''
You need to remove vowels from the entire sentence

'''
def remove_vowels(sentence):
    vowels = "aeıioöuüAEIİOÖUÜ"
    new_sentence ="" #we are going to sent our normal letters to this variable
    for i in sentence:
        if i not in vowels:
            new_sentence += i # we have sent our letters to this place
    return new_sentence #and we have called 
    
    
    
    
print(remove_vowels("Python problemi çözüyorum..."))
