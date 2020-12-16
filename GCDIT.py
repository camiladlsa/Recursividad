print("\nGCD Euclid's algorithm\n")
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return (x)
print("\nEl GCD es:",gcd(x,y),"\n")