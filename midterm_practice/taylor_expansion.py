import math

def taylor_exp(f, derivatives, a, x, n):
    """
    f: the function f(x)
    derivatives: list of derivative functions [f', f'', f''', ...]
    a: expansion point
    x: value to approximate
    n: number of terms (order)
    """
    result = f(a)
    for i in range(1, n + 1):
        term = derivatives[i-1](a) * ((x - a) ** i) / math.factorial(i)
        result += term
    return result

# Example: f(x) = e^x
f = lambda x: math.exp(x)
derivatives = [
    lambda x: math.exp(x),  # f'(x)
    lambda x: math.exp(x),  # f''(x)
    lambda x: math.exp(x),  # f'''(x)
    lambda x: math.exp(x)   # f''''(x)
]

approx = taylor_exp(f, derivatives, a=0, x=0.1, n=4)
print(f"Approximation of e^0.1 ≈ {approx}")
print(f"Actual value = {math.exp(0.1)}")
