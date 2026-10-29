def extended_gcd(a, b):
    ''''
    a(x) and b(x) and deg(b(x)) <= deb(a(x))
    quotient q1(x) and remainder r1(x) (1st iteration)
    Repeat until bn(x) = 0
    '''
    old_r = a
    r = b
    old_s = 1
    s = 0
    old_t = 0
    t = 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_r, old_s, old_t


a, b = 12, 12
gcd, x, y = extended_gcd(a, b)
print(f'extended_gcd({a}, {b}) = ({gcd}, {x}, {y})')
print(f"Bezout's identity: {a} * {x} + {b} * {y} = {a * x + b * y}")
assert a * x + b * y == gcd
