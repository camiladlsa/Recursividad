print("\nGCD Euclid's algorithm\n")

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

def gcd(x,y):

    if y == 0:
        return x
    else:
        return gcd(y, x % y)

print("\nEl GCD es: ", gcd(x,y),"\n")