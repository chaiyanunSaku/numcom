def bisection(f, a, b, tol=1e-5, max_iter=100):
    """
    f: the function
    a, b: initial interval [a, b] where f(a)*f(b) < 0
    tol: tolerance for stopping
    max_iter: maximum number of iterations
    """
    if f(a) * f(b) >= 0:
        print("Bisection method fails: f(a) and f(b) must have opposite signs.")
        return None
    
    for i in range(max_iter):
        m = (a + b) / 2
        fm = f(m)
        print(f"Iteration {i+1}: a={a}, b={b}, m={m}, f(m)={fm}")
        
        if abs(fm) < tol:  # found root
            return m
        
        if f(a) * fm < 0:
            b = m  # root is in [a, m]
        else:
            a = m  # root is in [m, b]
    
    return (a + b) / 2  # return best approximation if max_iter reached

# Example usage:
def f(x):
    return x**3 - x - 2

root = bisection(f, 1, 2)
print(f"Approximate root: {root:.5f}")
