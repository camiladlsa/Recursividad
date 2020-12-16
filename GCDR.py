print("\nGCD Euclid's algorithm\n")

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

def gcd(x, y):
    if y > x:
        return gcd(y, x)
    if x % y == 0:
        return y
    return gcd(y, x % y)  

print("\nEl GCD es:",gcd(x,y),"\n")