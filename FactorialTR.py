n = int(input("\nIngrese un entero positivo para tomar el factorial: "))

def factorial(n):

	if not isinstance(n, int):
		print("Error: el valor debe ser un entero\n")
	elif n < 0:
		print("\nError: el factorial no existe para n < 0.\n")
	else:
		return factorial_process(n, 1);

def factorial_process(n, accm):
    if n == 0:
        return accm
    else:
    	return factorial_process(n - 1, n * accm)

print("\nFactorial:",factorial(n),"\n")