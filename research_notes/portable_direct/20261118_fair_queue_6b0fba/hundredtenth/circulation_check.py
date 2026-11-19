"""Rational checks for the six-axis critical circulation law; no simulation."""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations
import json
from math import comb, factorial
from pathlib import Path
import runpy

EDGES = tuple(combinations(range(6), 2))
SIGNED = 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
SIGNED_SHA256 = '6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4'


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def mv(m, x):
    return [dot(row, x) for row in m]


def outer_diff(u, v):
    return [[a*d-b*c for c,d in zip(u,v)] for a,b in zip(u,v)]


def integral(poly):
    return sum(c*F((-1)**j*factorial(j), (i+1)**(j+1)) for (i,j),c in poly.items())


def primitive(poly):
    out = defaultdict(F)
    for (i,j),c in poly.items():
        for k in range(j+1):
            out[i+1,j-k] += c*F((-1)**k*factorial(j),factorial(j-k)*(i+1)**(k+1))
    return out


def centered(poly):
    p = defaultdict(F,poly)
    p[0,0] -= integral(p)
    return {key:v for key,v in p.items() if v}


def norm2(poly):
    square = defaultdict(F)
    for (i,j),c in poly.items():
        for (k,l),v in poly.items():
            square[i+k,j+l] += c*v
    return integral(square)


def word_stats(rates, counts, mat):
    """Distribution moments of raw sum, conditioned on first remaining letter."""
    @lru_cache(None)
    def recurse(left):
        rem = dot(left,rates)
        if rem == 0:
            return (F(1),F(0),F(0),F(0),F(0))
        sums = [F(0) for _ in range(5)]
        for j, amount in enumerate(left):
            if not amount:
                continue
            prob = F(amount*rates[j],rem)
            add = sum(F(mat[i][j]*(counts[i]-left[i]), counts[i]*counts[j]) for i in range(j))
            nxt = list(left)
            nxt[j] -= 1
            tail = recurse(tuple(nxt))
            for k in range(5):
                sums[k] += prob * sum(comb(k,l)*add**(k-l)*tail[l] for l in range(k+1))
        return tuple(sums)
    return recurse(tuple(counts))


def finite_row(eps, h, counts, mat, signed):
    rates = [1+eps*x for x in h]
    raw = word_stats(rates,counts,mat)
    avg = sum(F(mat[i][j]*rates[i],rates[i]+rates[j]) for i,j in EDGES)
    assert raw[0] == 1 and raw[1] == avg
    def k(a,b,c):
        return F(a*b*c,(a+b+c)*(a+b)*(a+c))
    def rr(a,b):
        return F(a*b*(a*a+a*b+b*b),(a+b)**2*(a+2*b)*(2*a+b))
    one = sum(F(mat[i][j]*mat[i][l],counts[i])*k(rates[i],rates[j],rates[l])
              for i in range(6) for j in range(6) for l in range(6))
    two = sum(F(mat[i][j]**2,counts[i]*counts[j])*rr(rates[i],rates[j]) for i,j in EDGES)
    var = raw[2]-avg**2
    assert var == one+two
    signed_target = [m*(-1)**i for i,m in enumerate(counts)]
    mult = signed['shortest_path_multiplicity'](signed_target)
    assert signed['shortest_event_count'](signed_target) == sum(counts)
    assert signed['endpoint_multiplicity'](sum(counts),signed_target) == mult
    fourth = sum(comb(4,j)*(-avg)**(4-j)*raw[j] for j in range(5))
    row = dict(epsilon=str(eps), rates=[str(a) for a in rates], target=signed_target,
               number_of_axis_words=mult, raw_mean=str(avg),
               half_center_drift=str(avg-F(sum(mat[i][j] for i,j in EDGES),2)),
               variance=str(var), fourth_cumulant=str(fourth-3*var**2))
    if counts == (1,)*6:
        law = defaultdict(F)
        for word in permutations(range(6)):
            prob,rem = F(1),sum(rates)
            for j in word:
                prob *= F(rates[j],rem)
                rem -= rates[j]
            raw_score = sum(mat[i][j] for i,j in EDGES if word.index(i)<word.index(j))
            law[raw_score] += prob
        assert all(sum(v*x**k for x,v in law.items()) == raw[k] for k in range(5))
        assert mult == factorial(6)
        row.update(direct_six_letter_score_bins=len(law))
    return row


def decimal_interval(lo, hi, places=12):
    scale = 10**places
    return {'decimal_places':places, 'lower_integer':lo*scale//1,
            'upper_integer':-((-hi*scale)//1)}


def check_example(name, d, slopes, mat, signed):
    powers = [[h**k for h in slopes] for k in range(2*d+3)]
    assert all(not any(mv(mat,v)) for v in powers[:d])
    b = mv(mat,powers[d])
    assert any(b)
    size = sum(mat[i][j]**2 for i,j in EDGES)
    mb2 = dot(mv(mat,b),mv(mat,b))
    assert mb2 == size*dot(b,b)  # these examples both have a single skew block
    cat = comb(2*d,d)//(d+1)
    drift = F(cat*dot(powers[d+1],b),2**(2*d+2))
    taylor = [sum(mat[i][j]*F((slopes[i]-slopes[j])*(-slopes[i]-slopes[j])**(k-1),
                              2**(k+1)) for i,j in EDGES) for k in range(1,2*d+2)]
    assert taylor == [0]*(2*d)+[drift]
    f = centered({(1,d):F(1,factorial(d))})
    rho = [norm2(f)]
    for _ in range(6):
        f = centered(primitive(f))
        rho.append(norm2(f))
    V = dot(b,b)*rho[0]
    cross = 2*mb2*rho[1]
    fourth = F(size**2,120)+6*cross   # t=1
    assert 0 < cross and V > 0
    out = dict(name=name, d=d, b=b, skew_block_strength_squared=size,
               drift_first_possible=str(drift), critical_linear_variance=str(V),
               equal_rate_quadratic_variance=str(F(size,12)),
               covariance_of_squares=str(cross), critical_fourth_cumulant=str(fourth),
               spectral_primitive_norms_squared=list(map(str,rho)),
               actual_path_rows=[finite_row(e,slopes,m,mat,signed) for e,m in [
                   (F(0),(1,)*6),(F(1,8),(1,)*6),(F(-1,9),(1,2,1,2,1,1))]])
    # At z=1/sigma, t=1, (1+x)^-1 is bracketed by its degree 5/6 sums.
    vlo = dot(b,b)*sum((-1)**k*rho[k] for k in range(6))
    vhi = vlo+dot(b,b)*rho[6]
    xlo, xhi = vlo/(2*size),vhi/(2*size)
    assert 0 < xlo <= xhi < 1
    def exp_minus(x, deg):
        return sum((-x)**k/factorial(k) for k in range(deg+1))
    half = F(1,2)
    sh_lo = sum(half**j/factorial(j) for j in range(1,20,2))
    sh_hi = sh_lo+2*half**21/factorial(21)
    out['critical_cf_at_inverse_block_strength'] = decimal_interval(
        half/sh_hi*exp_minus(xhi,19), half/sh_lo*exp_minus(xlo,20))
    return out


def main(repo):
    data = (repo/SIGNED).read_bytes()
    assert sha256(data).hexdigest() == SIGNED_SHA256
    signed = runpy.run_path(str(repo/SIGNED))
    slopes = tuple(range(6))
    tri = outer_diff((1,-1,0,0,0,0),(0,1,-1,0,0,0))
    high = outer_diff((1,-4,6,-4,1,0),(0,1,-4,6,-4,1))
    records = [check_example('triangle',1,slopes,tri,signed),
               check_example('fourth_differences',4,slopes,high,signed)]
    assert records[0]['drift_first_possible'] == '-1/8'
    assert records[1]['drift_first_possible'] == '-315/8'
    assert records[1]['critical_linear_variance'] == '363979/972'
    return dict(task='RS-X6-WEIGHTED-CIRCULATION-CANCELLATION',
                source_signed_kernel_sha256=SIGNED_SHA256,
                critical_parameter_for_cumulants_and_cf=1,
                examples=records)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd(),help='checkout containing the pinned signed kernel')
    print(json.dumps(main(parser.parse_args().repo),indent=2,sort_keys=True))
