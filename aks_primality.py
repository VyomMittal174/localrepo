import math

def is_perfect_power(n):
    for b in range(2, int(math.log2(n)) + 2):
        a = int(round(n ** (1 / b)))
        if a ** b == n:
            return True
    return False

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_order(n, r):
    for k in range(1, r):
        if pow(n, k, r) == 1:
            return k
    return -1

def is_prime_aks(n):
    print(f"Checking if {n} is prime using AKS...")
    
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Step 1: Check if n is a perfect power
    if is_perfect_power(n):
        print("Composite: Perfect power")
        return False

    # Step 2: Find the smallest r such that ord_r(n) > log(n)^2
    max_k = math.log2(n) ** 2
    r = 2
    while True:
        if gcd(n, r) == 1:
            order = multiplicative_order(n, r)
            if order > max_k:
                break
        r += 1

    # Step 3: Check for a < r if gcd(a, n) > 1, then composite
    for a in range(2, r + 1):
        if 1 < gcd(a, n) < n:
            print(f"Composite: gcd({a}, {n}) > 1")
            return False

    # Step 4: Polynomial test (slower part)
    for a in range(1, int(math.sqrt(totient(r)) * math.log2(n)) + 1):
        lhs = (pow(x_minus_a(n, a), n, n, r))
        rhs = (pow(x, n, n, r) - a) % n
        if lhs != rhs:
            print(f"Composite: Failed congruence for a = {a}")
            return False

    print("Probably Prime (passed AKS test)")
    return True

# Simplified polynomial ring operations (mod x^r - 1, mod n)
def x_minus_a(n, a):
    return lambda x: (x - a) % n

def pow_poly(poly_func, exp, mod_n, mod_r):
    # Naive exponentiation for small examples
    res = lambda x: 1
    for _ in range(exp):
        temp = res
        res = lambda x, t=temp: (t(x) * poly_func(x)) % mod_n
    return res

def totient(n):
    result = n
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result

# Example usage
n = int(input("Enter a number to test for primality: "))
result = is_prime_aks(n)
print(f"\nResult: {'Prime' if result else 'Composite'}")
