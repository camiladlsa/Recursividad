n = int(input("\nIngrese un entero positivo para tomar el factorial: "))

def factorial(n): 
    res = 1; 
    for i in range(1, n + 1): 
        res *= i; 
    return res; 
  
if n < 0:
   print("\nPerdón, el factorial no existe para n < 0.\n")
elif n == 0:
   print("\nEl factorial de 0 es 1.\n")
else:
   print("\nFactorial:",factorial(n),"\n")