"""Audit the actual carry, its dyadic energies, and a finite resonance example."""
from collections import defaultdict
import cmath
import json
import math


def primes(n):
    flags = bytearray(b'\1')*(n+1)
    flags[:2] = b'\0\0'
    for p in range(2, math.isqrt(n)+1):
        if flags[p]:
            flags[p*p::p] = b'\0'*((n-p*p)//p+1)
    return [p for p, flag in enumerate(flags) if flag]


def valuation_factorial(n, p):
    count = 0
    while n:
        n //= p
        count += n
    return count


def divisor_sums(limit):
    tau = [0]*(limit+1)
    for d in range(1,limit+1):
        for n in range(d,limit+1,d):
            tau[n] += 1
    for j in range(1,limit+1):
        tau[j] += tau[j-1]
    return tau


def arithmetic_blocks(max_k):
    stop = 2**(max_k+1)
    limit = 2*stop
    divisor = divisor_sums(limit)
    psi = [0.]*(limit+1)
    prime_list = primes(limit)
    for p in prime_list:
        m = p
        while m <= limit:
            psi[m] = math.log(p)
            m *= p
    for n in range(1,limit+1):
        psi[n] += psi[n-1]
    checked = 0
    for n in range(1,193):
        carry = [0]+[2*n//m-2*(n//m) for m in range(1,n+1)]
        A = sum(carry)
        assert A == divisor[2*n]-2*divisor[n]-n
        for p in prime_list:
            if p > 2*n:
                break
            left, m, pn, p2n = 0, p, 0, 0
            while m <= 2*n:
                p2n += 1
                if m <= n:
                    left += n*carry[m]-A
                    pn += 1
                m *= p
            v = valuation_factorial(2*n,p)-2*valuation_factorial(n,p)
            assert left == n*(v-p2n)+(n-A)*pn
            checked += 1
    blocks = []
    for k in range(max_k+1):
        N = 2**k
        def square(n):
            alpha = (divisor[2*n]-2*divisor[n]-n)/n
            logbin = math.lgamma(2*n+1)-2*math.lgamma(n+1)
            J = logbin-psi[2*n]+(1-alpha)*psi[n]
            return (J/n)**2
        W = math.fsum(square(n) for n in range(N,2*N))
        blocks.append(W)
    return dict(max_k=max_k, prime_coefficient_equalities=checked, exact_integers_through=192,
                W_by_k=[round(x,9) for x in blocks],
                first_K_block_average={str(K):round(math.fsum(blocks[:K])/K,9)
                                       for K in (4,8,12,len(blocks))})


def resonance():
    # Frequencies measured in turns per log-2 block; quarter-integer numerators.
    rows = [(-5, 1, 2-1j), (-1, 2, 1+1j), (1, 2, 1-1j), (5, 1, 2+1j)]
    def integral(d):
        if d == 0:
            return 1
        if d % 4 == 0:
            return 0
        arg = 2j*math.pi*d/4
        return (cmath.exp(arg)-1)/arg
    point, block = [], []
    for k in range(4):
        point.append(abs(sum(m*c*(1j)**((a*k)%4) for a,m,c in rows))**2)
        total = sum(m*c*n*d.conjugate()*(1j)**(((a-b)*k)%4)*integral(a-b)
                    for a,m,c in rows for b,n,d in rows)
        assert abs(total.imag)<1e-10
        block.append(total.real)
    diagonal = sum(m*m*abs(c)**2 for _,m,c in rows)
    alias = defaultdict(complex)
    for a,m,c in rows:
        alias[a%4] += m*c
    assert abs(sum(block)/4-diagonal)<1e-10
    assert abs(sum(point)/4-sum(abs(x)**2 for x in alias.values()))<1e-10
    assert abs(sum(point)/4-diagonal)>1
    return dict(frequency_numerators_over_4=[a for a,m,c in rows],
                multiplicities=[m for a,m,c in rows], window_energy=[round(x,9) for x in block],
                point_sampling_mean=round(sum(point)/4,9), continuous_window_mean=round(diagonal,9))


def constants():
    euler = 0.57721566490153286061
    L = math.log(2)
    a = 2-2*L
    S1 = 2+euler-math.log(4*math.pi)
    S2 = 2*S1+math.log(4*math.pi)-1-1.5*math.log(3)
    # Independently integrate the explicit formula on 1<x<2 after u=1-t^2,
    # giving a continuous integrand t*log(2*t^2-t^4), t in [0,1/sqrt(2)].
    last = 2**16
    delta = (1/math.sqrt(2))/last
    integral = delta*math.fsum((t*math.log(2*t*t-t**4))
                                 for j in range(last) for t in [(j+.5)*delta])
    value = 2*(S1-L+math.log(2*math.pi)/2+integral)
    assert abs(value-S2)<1e-9
    return dict(S1=round(S1,14), S2=round(S2,14), S2_by_midpoints=round(value,10),
                lower_constant=round(L*((2+a*a)*S1-2*a*S2),14),
                numerical_quadrature_intervals=last)


if __name__ == '__main__':
    print(json.dumps(dict(arithmetic=arithmetic_blocks(16), finite_frequency_check=resonance(),
                          analytic_constants=constants()),indent=2))
