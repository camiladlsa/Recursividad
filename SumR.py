def Sum(n): 
    if n <= 1: 
        return n 
    return n + Sum(n - 1) 

n = int(input("\nIngrese el N: "))
print("\nSum:",Sum(n),"\n")