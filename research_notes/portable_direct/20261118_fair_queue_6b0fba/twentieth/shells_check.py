"""Published discovery band and small arithmetic shells; exact covariances, no simulation."""
from bisect import bisect_right
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def sieve(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = bytes(2)
    for d in range(2, isqrt(limit) + 1):
        if flags[d]:
            flags[d*d::d] = bytes((limit-d*d)//d + 1)
    return [d for d in range(2,limit+1) if flags[d]]


def band_of(y):
    # Distinct points 210 floor((65/64)^j).
    num, den, left = 1, 1, 0
    while True:
        right = 210*(num//den)
        if right > y:
            return left, right
        left = right
        num, den = 65*num, 64*den


def stratum(X, p):
    if p*p >= X:
        return 31
    with localcontext() as ctx:
        ctx.prec = 55
        u = Decimal(p).ln()/Decimal(X).ln()
        return max(0,min(31,int(32*(1+(u/(1-u)).ln()/Decimal(3).ln()))))


def log_interval(x):
    # For integer x >= 1, exact rational enclosure of ln x after binary rescaling.
    def atanh_series(z):
        series = sum(z**(2*j+1)/(2*j+1) for j in range(21))
        return 2*series, 2*series + 2*z**43/(43*(1-z*z))
    j = x.bit_length()-1
    v = Fraction(x,2**j)
    lo, hi = atanh_series((v-1)/(v+1))
    l2,h2 = atanh_series(Fraction(1,3))
    return j*l2+lo, j*h2+hi


def primitive_root_32_bounds(value):
    """Rational enclosure of the positive 32nd root by exact bisection."""
    lo, hi = Fraction(1,3), Fraction(1)
    for _ in range(28):
        mid = (lo+hi)/2
        if mid**32 < value:
            lo = mid
        else:
            hi = mid
    return lo, hi


def verify_bin(X,p,j):
    # bin j iff 3^((j-32)/32) <= ln(p)/(ln(X)-ln(p)) < 3^((j-31)/32).
    lp,up = log_interval(p)
    lx,ux = log_interval(X)
    lower,upper = lp/(ux-lp),up/(lx-up)
    w0=primitive_root_32_bounds(Fraction(3)**(j-32))
    w1=primitive_root_32_bounds(Fraction(3)**(j-31))
    assert w0[1] < lower < upper < w1[0]


def matrix_rank(matrix):
    mat = [[Fraction(x) for x in row] for row in matrix]
    pivot = 0
    for c in range(len(mat[0])):
        r = next((k for k in range(pivot,len(mat)) if mat[k][c]), None)
        if r is None:
            continue
        mat[pivot],mat[r] = mat[r],mat[pivot]
        for k in range(pivot+1,len(mat)):
            ratio = mat[k][c]/mat[pivot][c]
            mat[k] = [v-ratio*w for v,w in zip(mat[k],mat[pivot])]
        pivot += 1
    return pivot


def population_cov_num(rows):
    h = len(rows[0])
    return [[h*sum(a*b for a,b in zip(x,y))-sum(x)*sum(y)
             for y in rows] for x in rows]


def discovery_band():
    X, p = 3000000, 53
    for q, j in ((47,1),(53,2),(59,3)):
        verify_bin(X,q,j)
    assert [n for n in range(47,60) if prime(n)] == [47,53,59]
    first = X//p+1
    lo, hi = band_of(first)
    assert (lo,hi) == (56490,57330)
    h = (hi-lo)//210
    P = {n for n in range(lo,hi) if prime(n)}
    ps = sieve(hi-1)
    assert P == {q for q in ps if q >= lo}
    windows, profiles = [], []
    for a,b in ((1,100),(3,1000),(1,1000)):
        last = (X*(a+b)//b)//p
        assert first >= lo and last < hi
        windows.append([first,last])
        profile = [sum(lo+(n-lo-210*s)%(hi-lo) in P for n in range(first,last+1))
                   for s in range(h)]
        # Independently rotate the set, then intersect the actual interval.
        assert profile == [sum(first<=lo+(q-lo+210*s)%(hi-lo)<=last for q in P)
                           for s in range(h)]
        profiles.append(profile)
    cov = population_cov_num(profiles)
    a,b,c = cov[0]
    d,e,f = cov[1]
    g,i,j = cov[2]
    determinant = Fraction(a*(e*j-f*i)-b*(d*j-f*g)+c*(d*i-e*g),h**6)
    assert determinant == Fraction(81,64) and matrix_rank(cov) == 3
    blocks=[sum(lo+210*t<=q<lo+210*(t+1) for q in P) for t in range(h)]
    ranks={}
    for width in range(1,h+1):
        full=[sum(blocks[(s+t)%h] for t in range(width)) for s in range(h)]
        translated=[full[s:]+full[:s] for s in range(h)]
        ranks[width]=matrix_rank(population_cov_num(translated))
    assert ranks == {1:3,2:2,3:3,4:0}
    return dict(X=X,p=p,zero_based_bin=2,band=[lo,hi],windows=windows,profiles=profiles,
                covariance_numerators=cov,covariance_denominator=h*h,
                determinant=str(determinant),wheel_block_counts=blocks,aligned_window_ranks=ranks)


def toy_shell(X, upper):
    rows=sieve(isqrt(upper))
    qlist=sieve(upper//2)
    profile=[0]*32
    overflow, diagonal=0,0
    for p in rows:
        if p**4<=X:
            continue
        count=bisect_right(qlist,upper//p)-bisect_right(qlist,max(p,X//p))
        profile[stratum(X,p)]+=count
        overflow+=count*(p*p>X)
        diagonal+=int(X<p*p<=upper)
    independent=[0]*32
    independent_overflow=independent_diag=0
    for n in range(X+1,upper+1):
        p=next((d for d in range(2,isqrt(n)+1) if n%d==0),None)
        if p is None or p**4<=X or not prime(n//p):
            continue
        if p*p==n:
            independent_diag+=1
        else:
            independent[stratum(X,p)]+=1
            independent_overflow+=p*p>X
    assert (independent,independent_overflow,independent_diag) == (profile,overflow,diagonal)
    return dict(X=X,upper=upper,total=sum(profile),overflow=overflow,diagonal=diagonal,
                profile=profile)


def smooth_check():
    with localcontext() as ctx:
        ctx.prec=60
        one,three=Decimal(1),Decimal(3)
        log3=three.ln()
        w=[(log3*(Decimal(i)/32-1)).exp() for i in range(33)]
        coeff=[(2 if j==31 else 0)-(w[j+1]-w[j])-one/24 for j in range(32)]
        assert abs(sum(coeff)) < Decimal('1e-55')
        h=Decimal('0.00000001')
        interior=[(log3/32+((1+h*(1+w[j]))/(1+h*(1+w[j+1]))).ln())/(1+h)
                  for j in range(32)]
        over=(1+2*h).ln()/(1+h)
        total=(3+4*h).ln()/(1+h)
        assert abs(sum(interior)+over-total)<Decimal('1e-55')
        population=interior[:]
        population[-1]+=over
        assert all(population[i]>population[i+1] for i in range(30))
        assert min(population[31]-z for z in population[:31])>0
        # Differentiate the exact normalized profile numerically at h=0.
        err=max(abs((population[j]/total-one/32)/h - coeff[j]/log3) for j in range(32))
        assert err < 10*h
        return dict(coeff_first=str(+coeff[0])[:19],coeff_last_interior=str(+coeff[30])[:19],
                    coeff_folded_last=str(+coeff[31])[:19],max_derivative_error=str(err))


if __name__=='__main__':
    print(json.dumps(dict(discovery=discovery_band(),toy=[toy_shell(X,101*X//100)
                         for X in (10000,227**2-1,100000)],smooth=smooth_check()),indent=2))
