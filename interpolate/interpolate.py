# ZERO = Polynomial([])

# f = Polynomial([1,2,3]) # 1 + 2x + 3x^2
# g = Polynomial([-8, 17, 0, 5]) 

# f + g == Polynomial([-7, 19, 3, 5])
# f(1) == 6

from interpolate.polynomial import ZERO, Polynomial


def interpolate(points):
    """ Return the unique polynomial of degree at most n
    passing through the given n + 1 points
    """
    if len(points) == 0:
        raise ValueError('Must provide at least one point.')
    x_vals = [p[0] for p in points]
    if len(set(x_vals)) < len(x_vals):
        raise ValueError('Not all x values are distinct.')
    terms = [single_term(points, i) for i in range(len(points))]
    # Sum all the terms using zero polynomial as the start value
    return sum(terms, ZERO)

def single_term(points, i):
    """Return one term of an interpolated polynomial
    Args:
    - points: a list of (float, float)
    - i: an integer indexing a specific point
    """
    term = Polynomial([1.]) # What??
    xi, yi = points[i]

    for j, p in enumerate(points):
        if j == i:
            continue
        xj = p[0]
        term = term * Polynomial([-xj / (xi - xj), 1.0 / (xi - xj)])

    return term * Polynomial([yi])
