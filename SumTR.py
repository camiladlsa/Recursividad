n = int(input("\nIngrese el N: "))

def sum_tr(m, n):
    if m == 1:
        return n
    return sum_tr(m - 1, m + n)

def sum(n):
    return sum_tr(n, 1)

print("\nSum:",sum(n),"\n")