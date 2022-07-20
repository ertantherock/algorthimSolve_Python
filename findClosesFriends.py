#PROBLEM EXPLANATION
#Vural and Fatih are close friends. If they are next to each other in the list, the function should return True. 
#It should return False if there are names among them.

def arkadas(liste):
    if liste.index("Vural") == liste.index("Fatih")+1:
        return True
    elif liste.index("Vural") == liste.index("Fatih")-1:
        return True
    else:
        return False
