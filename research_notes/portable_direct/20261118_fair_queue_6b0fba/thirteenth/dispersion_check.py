"""Finite checks for the three cubic dispersion terms and the local density kernel.

Run with Python 3.10+ and no external dependencies. Gauss sums use complex
floating point. All local probability and norm-square checks use fractions.
"""
from cmath import exp
from fractions import Fraction as F
from itertools import combinations, product
import json
from math import gamma, pi, sqrt


def multiply(z, w):
    a, b = z
    c, d = w
    return (a*c-b*d, a*d+b*c-b*d)


def norm(z):
    a, b = z
    return a*a-a*b+b*b


def power(z, n):
    out = (1, 0)
    for _ in range(n):
        out = multiply(out, z)
    return out


primes = [(1, 3), (4, 3), (-2, 3)]  # norms 7, 13, 19; all primary
omega = exp(2j*pi/3)


def element(factors):
    out = (1, 0)
    for p in factors:
        out = multiply(out, p)
    return out


def exponent(z, factors):
    value = 0
    for x, y in factors:
        p = norm((x, y))
        r = -x*pow(y, -1, p) % p
        residue = (z[0]+z[1]*r) % p
        if not residue:
            return None
        symbol = pow(residue, (p-1)//3, p)
        value += [1, r, r*r % p].index(symbol)
    return value % 3


def chi(z, factors):
    e = exponent(z, factors)
    return 0 if e is None else omega**e


def gauss(factors):
    # At these split primes the rational integers give complete residues
    # also at powers; avoid using two conjugate primes over the same p.
    z = element(factors)
    n = norm(z)
    return sum(chi((k, 0), factors)*exp(2j*pi*((k*(2*z[0]-z[1])) % n)/n)
               for k in range(n))/sqrt(n)


def check_gauss():
    labels = [(), (primes[0],), (primes[1],), (primes[2],),
              (primes[0],primes[1]), (primes[0],primes[0])]
    values = {label: gauss(label) for label in labels}
    assert all(abs(abs(v)-int(len(set(label))==len(label)))<2e-11
               for label,v in values.items())
    tested = 0
    for a in labels[:4]:
        for b in labels[:4]:
            assert abs(gauss(a+b)-values[a]*values[b]*chi(element(a),b).conjugate())<2e-11
            tested += 1
    beta = {labels[1]:2+1j, labels[2]:-1+2j, labels[4]:1-2j}
    scalar = sum(v*norm(element(b))**(-1/6) for b,v in beta.items())
    c = (2*pi)**(2/3)/(3*gamma(2/3))
    raw = 0; mixed = 0j; model = 0; direct = 0
    for a in labels:
        z = element(a)
        t = norm(z)**(-1/6)
        f = sum(v*values[b]*chi(z,b).conjugate() for b,v in beta.items())
        cross = sum(v*gauss(a+b) for b,v in beta.items())
        assert abs(cross-values[a]*f)<2e-10
        sf = int(len(set(a))==len(a))
        m = c*scalar*values[a].conjugate()*t
        raw += sf*abs(f)**2
        mixed += sf*c*scalar.conjugate()*t*cross
        model += sf*abs(m)**2
        direct += sf*abs(f-m)**2
    assert abs(direct-(raw-2*mixed.real+model))<2e-10
    return dict(pair_identities=tested, signed_coefficients=[1,-2,1],
                complex_inputs=len(beta), direct_corrected_energy=round(direct,9))


def check_cubes():
    # Distinct orbit representatives for x^3 under the three cube roots of 1.
    jset = [(x,y) for x in range(-9,10) for y in range(-9,10)
            if 0<norm((x,y))<=48]
    for d in [(1,0),primes[0],multiply(*primes[:2])]:
        counts = {}
        for j in jset:
            h = multiply(power(d,2),power(j,3))
            counts[h] = counts.get(h,0)+1
            assert multiply(d,h)==power(multiply(d,j),3)
            # Trace(h/(3 sqrt(-3))) equals the omega-coordinate of h / 3.
            assert h[1] % 3 == 0
        assert set(counts.values())=={3}
    # Independent Gaussian transform normalization (a Schwartz test).
    ratio = 2/(3*sqrt(3))*4**(-1/3)*pi**(1/3)*gamma(1/3)/gamma(2/3)
    assert abs(ratio-(2*pi)**(4/3)/(9*gamma(2/3)**2))<2e-14
    return dict(nonzero_roots=len(jset), frequencies_per_d=len(jset)//3,
                phase_and_multiplicity_tested_for_d=3)


def subsets(s):
    return [frozenset(row) for k in range(len(s)+1) for row in combinations(s,k)]


def prod(values):
    result=F(1)
    for x in values:
        result*=x
    return result


def check_local():
    # Includes an inert prime (norm 4) as well as split prime ideals.
    P=(4,7,13,19)
    family=subsets(P)
    rho=lambda B:prod(F(q,q+1) for q in B)
    weight=lambda J:prod(F(1 if q in J else q,q+1) for q in P)
    assert sum(weight(J) for J in family)==1
    w={B:(F((i*5)%9-4),F((i*3)%7-2)) for i,B in enumerate(family)}
    mu2norm=lambda v:v[0]**2+v[1]**2
    def coefficient(Bs,f):
        return tuple(sum((w[B][i]*f(B) for B in Bs),F()) for i in (0,1))
    total=sum(weight(J)*mu2norm(coefficient([B for B in family if not B&J],lambda _:1))
              for J in family)
    for B,C in product(family,repeat=2):
        k=sum(weight(J) for J in family if not J&(B|C))
        assert k==rho(B|C)==rho(B)*rho(C)*sum(1/prod(d) for d in subsets(B&C))
    terms={d:mu2norm(coefficient([B for B in family if d<=B],rho))/prod(d)
           for d in family}
    assert sum(terms.values())==total
    var=total-terms[frozenset()]
    assert var>0
    q=7
    bad=F(1,q+1)
    assert bad*(bad**2)==F(1,512)
    return dict(local_kernel_entries=len(family)**2, subset_error_terms=len(terms)-1,
                coherent_field_second_moment=str(total), local_variance=str(var),
                common_prime_bad_slice_share=str(bad), relative_three_density_factors="1/512")


if __name__=='__main__':
    print(json.dumps(dict(gauss=check_gauss(),cubes=check_cubes(),local=check_local()),
                     indent=2))
