import math

# Original function
def f(x):
    return math.exp(x)

# Derivatives
def f1(x):
    return math.exp(x)  # f'(x)

def f2(x):
    return math.exp(x)  # f''(x)

def f3(x):
    return math.exp(x)  # f'''(x)

def f4(x):
    return math.exp(x)  # f''''(x)

# List of derivative functions
derivatives = [f1, f2, f3, f4]

# Taylor expansion function
def taylor_exp(f, derivatives, a, x, n):
    result = f(a)
    for i in range(1, n + 1):
        term = derivatives[i-1](a) * ((x - a) ** i) / math.factorial(i)
        result += term
    return result

# Example: approximate e^0.1 around a=0, 4th order
approx = taylor_exp(f, derivatives, a=0, x=0.1, n=4)
print(f"Approximation of e^0.1 ≈ {approx}")
print(f"Actual value = {math.exp(0.1)}")
