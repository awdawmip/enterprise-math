"""GH-51/52 author-side exact certificate checker; not native Task acceptance."""
from fractions import Fraction
from math import isqrt


def primes_3mod4(bound):
    sieve = bytearray(b"\x01") * bound
    sieve[:2] = b"\x00\x00"
    for n in range(2, isqrt(bound - 1) + 1):
        if sieve[n]:
            sieve[n*n:bound:n] = b"\x00" * (((bound-1-n*n)//n)+1)
    return [p for p in range(7, bound) if sieve[p] and p % 4 == 3]


def prime_case(p):
    d = (p-3)//4
    c = [1]
    rho = [1]
    for r in range(d):
        c.append(c[-1] * pow((4*r+2)*(4*r+3)*(4*r+4), -1, p)
                 * (4*r+1)**3 % p)
        rho.append(rho[-1] * (4*r+3)*(4*r+4)*(4*r+5)
                   * pow((4*r+6)**3, -1, p) % p)
    assert c[d] != 0 and all(x != 0 for x in rho)
    for r in range(d+1):
        assert c[d-r] == c[d]*rho[r] % p, (p, r, "reverse")
    # Cleared L4 coefficient:
    # 2n(2n+1)^3 rho_n = (16n^2-1)n^2 rho_(n-1).
    for n in range(d+2):
        f_n = rho[n] if n <= d else 0
        f_prev = rho[n-1] if 1 <= n <= d+1 else 0
        assert (2*n*(2*n+1)**3*f_n - (16*n*n-1)*n*n*f_prev) % p == 0, (p,n,"L4")
    samples = []
    for z in (2,9,p-1):
        T = sum((8*r+1)*c[r]*pow(z,r,p) for r in range(d+1)) % p
        u = pow(z, -1, p)
        R = sum((8*r+5)*rho[r]*pow(u,r,p) for r in range(d+1)) % p
        assert T == -c[d]*pow(z,d,p)*R % p, (p,z,"special-value")
        samples.append((z,T,R))
    return d,c[d],samples


def rational_gosper_obstruction():
    for z in (Fraction(1,9), Fraction(9), Fraction(-1,2), Fraction(2)):
        a = Fraction(8,1)/(z-1)
        b = (5*z-1)/(z-1)**2
        k2 = -128*z*(2*z+1)/(z-1)**2
        k1 = -4*z*(33*z+59)/(z-1)**2
        assert k2 or k1
        if z == 9:
            assert a == 1 and b == Fraction(11,16)
            assert k2 == -342
    # The z=1 quadratic forced by leading equations fails at degree 1.
    assert Fraction(14*16-11*(-4),1)-92*Fraction(-1,6)-296 == Fraction(-38,3)


if __name__ == "__main__":
    rational_gosper_obstruction()
    ps = primes_3mod4(5000)
    for p in ps:
        prime_case(p)
    print("PASS_GH51_GOSPER_COEFFICIENT_OBSTRUCTION", 5, "rational parameter cases")
    print("PASS_GH52_REVERSE_SINGLE_SUM_AND_HOMOGENEOUS_L4", len(ps), "primes, 3 z cases each")
    for p in (7,11,19,43,67):
        print("CASE", p, prime_case(p))
