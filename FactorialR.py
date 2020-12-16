n = int(input("\nIngrese un entero positivo para tomar el factorial: "))

def factorial(n):
	if n == 1:
		return n
	else:
		return n*factorial(n-1)

if n < 0:
   print("\nPerdón, el factorial no existe para n < 0.\n")
elif n == 0:
   print("\nEl factorial de 0 es 1.\n")
else:
   print("\nFactorial:",factorial(n),"\n")