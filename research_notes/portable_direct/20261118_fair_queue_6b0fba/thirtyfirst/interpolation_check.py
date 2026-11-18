"""Finite arithmetic, exact Schur budgets and endpoint quadrature for 090-B."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from urllib.request import urlopen
import argparse
from itertools import product
from math import gcd, isqrt, pi
import cmath
import json


def norm(x, y):
    return x*x + x*y + y*y


def local_representatives(q):
    reps = {}
    for x, y in product(range(q), repeat=2):
        reps.setdefault(norm(x, y) % q, (x, y))
    return reps


def crt(a, u, b, v):
    return a + u * ((b-a)*pow(u, -1, v) % v)


def shell_phases():
    indices = [0,1,3,4,7,9,12,13,16,19,21,25,27,28,31]
    u, v = 13, 701
    for p in (u, v):
        assert all(p % t for t in range(2, isqrt(p)+1))
    m = u*v
    small = local_representatives(36)
    left, right = local_representatives(u), local_representatives(v)
    assert sorted(small) == indices and len(left) == u and len(right) == v
    assert len({6250*36*j % m for j in range(m)}) == m
    digest, count, maximum = sha256(), 0, 0
    for k in range(m):
        xy = [crt(a, u, b, v) for a, b in zip(left[k%u], right[k%v])]
        for r in indices:
            x, y = [crt(a, 36, b, m) for a, b in zip(small[r], xy)]
            value = norm(x, y)
            assert value % 36 == r and value % m == k
            digest.update(f'{r},{k},{x},{y}\n'.encode())
            count += 1
            maximum = max(maximum, value)
    assert sum(indices) % 36 == 0 and len(indices) % 2 == 1
    return dict(residues=indices, P15=-1, local_image_sizes=[len(small),len(left),len(right)],
                pairs=count, witness_sha256=digest.hexdigest(), max_witness=maximum,
                phase_period_per_residue=m)


def genuine_shells():
    bound = 1_000_000
    geometric = bytearray(bound+1)
    for x in range(isqrt(bound)+1):
        for y in range(isqrt(bound)+1):
            n = norm(x, y)
            if n > bound:
                break
            geometric[n] = 1
    geometric[0] = 0
    prime = bytearray([1])*(bound+1)
    prime[0:2] = bytes(2)
    for p in range(2,isqrt(bound)+1):
        if prime[p]:
            prime[p*p::p] = bytes((bound-p*p)//p+1)
    euler = bytearray([1])*(bound+1)
    euler[0] = 0
    for p in range(2, bound+1, 3):
        if not prime[p]:
            continue
        power = p
        while power <= bound:
            for q in range(1,bound//power+1):
                if q % p:
                    euler[q*power] = 0
            power *= p*p
    assert euler == geometric
    weights = [[F(1,4),F(3,8),F(0),F(3,8)],
               [F(1,9) if x==0 else F(2,9) if x in (1,3,4,7) else F(0) for x in range(9)],
               [F(1,13)]*13, [F(1,701**2)]+[F(702,701**2)]*700]
    for arr in weights:
        assert sum(arr)==1
    return dict(bound=bound, distinct_positive_norms=sum(geometric),
                zero_mod_701=[n for n in range(701,bound+1,701) if geometric[n]],
                euler_equals_coordinate_enumeration=True, local_weight_masses=[str(sum(w)) for w in weights])


def budgets():
    N = [F('16.16'), F('3.89')]
    delta, b, beta, beta0 = F('2.3e-8'), 335, F('1.36e-10'), F('2.501e-10')
    # exp(-pi/5)<.54 follows from pi>3.14 and the positive Taylor terms here.
    v = F('3.14')/5
    assert (1+v+v*v/2+v**3/6)*F('.54') > 1
    assert F('.54')*F('2.5e-10')+F('7e-15') < beta
    trig = F('2.58')+F('2.80')-2*(F('.44')+F('.006'))
    rhs = [F('9.2e-29')+beta*trig+F('.88')*beta0,
           F('9.2e-29')+beta*trig+F('.012')*F('1.27e-7')]
    den = [1-delta-b*beta*n for n in N]
    d = F('8.1e-8')
    es = [(t+beta*n*d)/v for t,n,v in zip(rhs,N,den)]
    ef = [n*(d+b*t) for n,t in zip(N,es)]
    crit_f = (F('2e-5')-sum(n*b*t/v for n,t,v in zip(N,rhs,den)))/sum(n*(1-delta)/v for n,v in zip(N,den))
    crit_t = (F('6e-9')-sum(t/v for t,v in zip(rhs,den)))/sum(beta*n/v for n,v in zip(N,den))
    assert sum(es)/2 < F('1.483e-9') and sum(ef)/2 < F('4.451e-6')
    assert F('6.3455e-7') < crit_f < F('6.3456e-7') and crit_t>1
    return dict(schur_denominators=list(map(str,den)), individual_tail_upper=str(sum(es)/2),
                individual_finite_upper=str(sum(ef)/2), finite_residual_ceiling=str(crit_f),
                tail_residual_ceiling_on_d=str(crit_t), variable_finite_poles_bound=str(trig))


def spectral():
    h, H, B, t = F(17,50), F(27,50), F(4,3), F(5,6)
    x = B/(h*h+t*t)
    e, omega = h*x-h, -t*x
    eh = H*B/(H*H+t*t)-h
    xp = -2*t*x/(h*h+t*t)
    slope = complex(float(-h*xp),float(-x-t*xp))*pi
    assert H-h < e < eh and (36*omega/2).denominator == 9113
    assert gcd(6250,9113) == 1 and abs(float(omega))*3>4
    # The complex, scaled top-interval integral for the actual n=25 rational column.
    # Simpson quadrature is a floating check only. Cut at u=40, after scaling
    # u=m(t_*-t); the exact endpoint limit follows by integration by parts.
    hh, tt, bb = map(float,(h,t,B))
    def funcs(tau):
        xx = bb/(hh*hh+tau*tau)
        return pi*complex(hh-hh*xx,-tau*xx), (hh+1j*tau)*xx
    gstar,lstar = funcs(tt)
    samples = {}
    for m in (757,3601,18001):
        out = []
        M, cut = 4096, min(40., m/18)
        for j in (0,1):
            total, step = 0j, cut/M
            for k in range(M+1):
                u = k*step
                gw,lw = funcs(tt-u/m)
                weight = 1 if k in (0,M) else (4 if k%2 else 2)
                total += weight * u**j * lw/lstar * cmath.exp(m*(gw-gstar)+1j*pi*u*25/m)
            obs = step*total/3
            out.append(round(abs(obs*slope**(j+1)-1),8))
        samples[str(m)] = out
    assert max(samples['18001'])<.01 and all(samples['18001'][j]<samples['3601'][j]<samples['757'][j] for j in (0,1))
    return dict(X=str(x), damping_excluding_pi=str(e), phase_excluding_pi=str(omega),
                finite_Fourier_damping_excluding_pi=str(eh), slope_real_excluding_pi=str(-h*xp),
                endpoint_scaled_relative_errors_d_then_c=samples)


CHECKER_SHA = '5689152e970b652a8e40c3c120eda3b45320c8745968a5cb416fa9b9dbdc5385'
CHECKER_URL = ('https://raw.githubusercontent.com/openai/math/'
               'adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/'
               'An-atomic-certificate-for-triangular-lattice-universal-optimality-'
               'September-26-2026/verification/check_certificate.py')


def signed_tail(checker):
    raw = Path(checker).read_bytes() if checker else urlopen(CHECKER_URL, timeout=30).read()
    if sha256(raw).hexdigest() != CHECKER_SHA or not __debug__:
        raise ValueError('enable assertions and supply the pinned certificate checker')
    env = {'__name__': 'frozen_triangle_certificate'}
    exec(compile(raw, CHECKER_URL, 'exec'), env)
    P, I, G = (env[k] for k in ('P', 'I', 'G'))
    expo, eta, pi0, iq = (env[k] for k in ('expo', 'eta', 'Pi', 'iQ'))
    T, L, atoms = (env[k] for k in ('T', 'L', 'U'))
    waves = env['Waves'](env['h'], env['h'])
    value = P(0)
    for j, atom in enumerate(atoms):
        g = iq*pi0*waves.zeta[j]
        den = 1-expo(36*g)
        reciprocal = den.conj()/(den.x*den.x+den.y*den.y)
        for n in T:
            term = atom*waves.lam[j]*(env['d'](n)-g)*expo(g*n)*reciprocal/env['q'](n)
            value += env['Real'](term)
    a = pi0*eta
    decay = expo(-36*a)
    weight = -decay/(1-decay)
    alias_weights = []
    for r in L:
        z = weight*expo(-a*r)
        alias_weights.extend((-a*z, z))
    def bounds(v):
        unit = G//10**18
        return [v.l//unit, -((-v.h)//unit)]
    collected = []
    for i, matrix in enumerate(env['data']):
        row, = env['matmul']([alias_weights], matrix[:-1])
        low = env['vmin'](row)
        high = -env['vmin']([-c for c in row])
        approximate = I(low.l, high.h)+value*(P('.006') if i==0 else -P('.006'))
        error = P(22, 10**15)
        exact = approximate+I(-error.h,error.h)
        assert (exact.h < P(-161,10**12).l and exact.l>P(-248,10**12).h if i==0
                else exact.l>P(158,10**12).h and exact.h<P(247,10**12).l)
        collected.append(dict(alias=bounds(I(low.l,high.h)), approximate=bounds(approximate),
                              with_error=bounds(exact)))
    return dict(source_sha256=CHECKER_SHA, integer_interval_unit='1e-18',
                constant_d=bounds(value), sides=collected)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checker', help='local public check_certificate.py (default fetches the pinned file)')
    options = parser.parse_args()
    print(json.dumps(dict(shell_certificate=shell_phases(), schur=budgets(), spectral=spectral(), arithmetic=genuine_shells(),
                          signed=signed_tail(options.checker)),
                     ensure_ascii=False, indent=2, sort_keys=True))
