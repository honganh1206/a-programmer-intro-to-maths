import math


def gradient(f, x, h=1e-5):
    '''
    Central difference formula to approximately calculate derivatives
    with second-order accuracy O(h^2)
    '''
    result = []
    for i in range(len(x)):
        forward = x.copy()
        backward = x.copy()

        forward[i] += h
        backward[i] -= h

        derivative = (f(forward) - f(backward)) / (2 * h)

        result.append(derivative)

    return result

def gradient_descent(f, x0, alpha=0.1, tol=1e-6, max_iter=1000):
    x = x0.copy()
    history = [x.copy()]

    for k in range(max_iter):
        g = gradient(f, x)

        magnitude = sum(value**2 for value in g)**0.5

        if magnitude < tol:
            break

        x = [
            x[i] - alpha * g[i]
            for i in range(len(x))
        ]

        history.append(x.copy())

        # print(f"Iteration {k+1}: x={x}, f(x)={f(x)}")

    return x, f(x), history

invphi = (math.sqrt(5) - 1) / 2  # 1 / phi

def gss(f, a, b, tol):
    """
    Golden-section search
    to find the minimum of f on [a,b]

    * f: a strictly unimodal function on [a,b]

    Example:
    >>> def f(x): return (x - 2) ** 2
    >>> x = gss(f, 1, 5, tol=1e-6)
    >>> print(f"{x:.5f}")
    2.00000

    """
    while b - a > tol:
        c = b - (b - a) * invphi
        d = a + (b - a) * invphi
        if f(c) < f(d):
            b = d
        else:
            a = c
    return (b + a) / 2


def steepest_descent(f, x0, tol=1e-6, max_iter=1000):
    """
    Minimize f using a golden-section search for each step size.

    Minimize a quadratic with its minimum at the origin:
    >>> def quadratic(x): return x[0]**2 + 2*x[1]**2
    >>> def derivative(x): return [2*x[0], 4*x[1]]
    >>> point, value, history = steepest_descent(
    ...     quadratic, derivative, [2.0, 1.0])
    >>> all(abs(coordinate) < 1e-6 for coordinate in point)
    True
    >>> value < 1e-12
    True
    >>> history[0]
    [2.0, 1.0]

    Minimize a quadratic with its minimum at [3, -2]:
    >>> def shifted(x): return (x[0] - 3)**2 + 2*(x[1] + 2)**2
    >>> def shifted_derivative(x): return [2*(x[0] - 3), 4*(x[1] + 2)]
    >>> point, value, history = steepest_descent(
    ...     shifted, shifted_derivative, [0.0, 0.0])
    >>> all(abs(actual - expected) < 1e-6
    ...     for actual, expected in zip(point, [3, -2]))
    True
    >>> value < 1e-12
    True
    """
    x = x0.copy()
    history = [x.copy()]

    for k in range(max_iter):
        g = gradient(f, x)

        magnitude = sum(value**2 for value in g)**0.5

        if magnitude < tol:
            break

        d = [-value for value in g]

        alpha = gss(
            lambda alpha: f([
                x[i] + alpha * d[i]
                for i in range(len(x))
            ]),
            a=0,
            b=1,
            tol=tol
        )

        x = [
            x[i] - alpha * g[i]
            for i in range(len(x))
        ]

        history.append(x.copy())

        # print(f"Iteration {k+1}: alpha={alpha:.6f}, x={x}, f(x)={f(x):.6f}")

    return x, f(x), history

def f(x):
    return x[0]**2 + 2*x[1]**2


minimum, value, history = gradient_descent(
    f=f,
    x0=[2.0, 1.0],
    alpha=0.1
)

print("Minimum (Gradient descent):", minimum)
print("Value (Gradient descent):", value)

minimum, value, history = steepest_descent(
    f,
    x0=[2.0, 1.0]
)

print("Minimum (Steepest descent):", minimum)
print("Value (Steepest descent):", value)
