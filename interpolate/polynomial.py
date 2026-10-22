from itertools import zip_longest


def strip(L, elt):
    '''Strip all copies of element from the end of the list'''
    if len(L) == 0:
        return L
    i = len(L) - 1
    while i >= 0 and L[i] == elt:
        i -= 1
    return L[:i+1]

class Polynomial(object):
    """A class representing a polynomial as a list of coefficients with no trailing zeros.

    A degree zero polynomial means an empty list of coefficients (provided as the variable ZERO)

    Polynomials override the basic arithmetic operations
    """
    def __init__(self, coefficients):
        '''Create a new polynomial.
        The caller must provide a list of all coefficients, even those that are zero'''
        self.coefficients = strip(coefficients, 0)
        self.indeterminate = 'x'

    def add(self, other):
        new_coefficients = [
            # Aggregate elements into tuples in parallel
            sum(x) for x in zip_longest(self, other, fillvalue=0.)
        ]
        return Polynomial(new_coefficients)

    def __add__(self, other):
        return self.add(other)

    def multiply(self, other):
        # Get length of coeffs
        new_coefficients = [0] * (len(self) + len(other) - 1)
        for i, a in enumerate(self):
            for j, b in enumerate(other):
                new_coefficients[i + j] += a * b
        return Polynomial(strip(new_coefficients, 0))

    def __mul__(self, other):
        return self.multiply(other)

    def __len__(self):
        return len(self.coefficients)

    def __iter__(self):
        return iter(self.coefficients)

    def __repr__(self):
        return ' + '.join(['%s %s^%d' % (a, self.indeterminate, i) if i > 0 else '%s' % a
                           for i, a in enumerate(self.coefficients)])

    def evaluate_at(self, x):
        '''Evaluate the polynomial at an input point using Horner's method'''
        sum = 0
        for c in reversed(self.coefficients):
            sum = sum * x + c
        return sum

    def __call__(self, *args, **kwds):
        '''Let Polynomial to be used like a function'''
        return self.evaluate_at(args[0])


ZERO = Polynomial([])
