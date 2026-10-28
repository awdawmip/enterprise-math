"""D25 original weighted-216 finite endpoint and Gosper search obstruction.
Portable, exact integer and finite-field certificate. Not a native H0/B0 execution.
"""
from math import comb

PRIMES = (5, 7, 11, 13, 19, 31, 37, 43, 61, 67, 73, 211, 373)


def a(n):
    return (2*n + 1)*(3*n + 1)*(3*n + 2)


def b(n):
    return 36*(n + 1)**3


def g(n):
    return 66*n*n + 113*n + 49


def R(n):
    return 4 - 12*n


# Both sides have polynomial degree <=4. Five distinct integer inputs certify
# the exact coefficient identity over Q (and hence its p-local forms).
for k in range(5):
    assert a(k)*R(k+1) - b(k)*R(k) - b(k)*(6*k+1) == -4*g(k)


def check(p):
    mod = p**3
    inv216 = pow(216, -1, mod)
    terms = [comb(2*k, k)**2*comb(3*k, k)*pow(inv216, k, mod)%mod
             for k in range(p)]
    # Independent forward hypergeometric recursion, with exact p-unit checks.
    recursive = [1]
    for k in range(p-1):
        recursive.append(recursive[-1]*a(k)*pow(b(k), -1, mod)%mod)
    assert recursive == terms
    wp = sum((6*k+1)*terms[k] for k in range(p)) % mod
    tp = comb(2*p,p)**2*comb(3*p,p)*pow(inv216, p, mod) % mod
    # Wolstenholme/Ljunggren boundary, p>=5; independently calculate t_p.
    assert tp == 12*pow(inv216, p, mod) % mod
    boundary = (R(p)*tp-R(0))%mod
    residual = 0
    last = None
    for k in range(p):
        if k<p-1:
            value = g(k)*terms[k]*pow(9*(k+1)**3, -1, mod) % mod
        else:
            numer = comb(2*k,k)**2*comb(3*k,k)
            assert numer % (p**3) == 0
            value = g(k)*(numer//(p**3))*pow(9*pow(216,k,mod),-1,mod)%mod
            last = value
        residual = (residual+value)%mod
    assert (boundary+residual)%mod == wp
    assert (R(p)*tp + last)%p == 0
    assert last%p == (-2*pow(9,-1,p))%p
    if p % 24 in (13,19):
        assert wp == p  # finite regression only; not universal proof
    return (p,wp,boundary,residual,tp,last)


# Original global F_p rational telescoper would need at least 2m distinct poles
# for p=6m+1, by the proven pole-orbit argument. Check its exact root distances.
for p in PRIMES:
    if p%6==1:
        m=(p-1)//6
        starts=(pow(2,-1,p),(2*pow(3,-1,p))%p,pow(3,-1,p))
        terminal=p-1
        assert min((terminal-z)%p for z in starts)==2*m-1
    print('CERT', *check(p))
print('PASS_D25_ORIGINAL216_GOSPER_POLE_BOUNDARY 13 exact primes')
