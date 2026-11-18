"""Exact local enumeration, geometric samples and rational Euler product enclosures."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt
import json


def norms(x, y, shear=0):
    u = x + shear * y
    return x*x + y*y, u*u - u*y + y*y


def prime_mask(limit):
    ok = bytearray([1]) * (limit + 1)
    ok[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if ok[p]:
            ok[p*p::p] = bytes(len(range(p*p, limit+1, p)))
    return ok


def primes_to(limit):
    return [i for i, prime in enumerate(prime_mask(limit)) if prime]


def root_lists(p, exponent=2):
    modulus = p**exponent
    return [[x for x in range(modulus) if norms(x, 1)[c] % modulus == 0] for c in range(2)]


def local_grid(p):
    """Count on the whole primitive part of the square residue grid, with no slope parameterization."""
    mod = p*p
    primitive = [0,0,0,0]
    for x, y in product(range(mod), repeat=2):
        if x % p or y % p:
            a, b = norms(x,y)
            primitive[(a%mod==0)+2*(b%mod==0)] += 1
    nc = [2*int(p%4==1), 2*int(p%3==1)]
    total = mod*(mod-1)
    expected = [total-sum(nc)*p*(p-1), nc[0]*p*(p-1), nc[1]*p*(p-1), 0]
    assert primitive == expected
    return primitive


def valuation_tests():
    tests = 0
    for p in (2,3,5,7,11,13,17,19):
        for j in (1,2,3):
            roots = root_lists(p,j)
            expected = [2*int(p%4==1)+int(p==2 and j==1),
                        2*int(p%3==1)+int(p==3 and j==1)]
            assert [len(z) for z in roots] == expected
            assert not set(roots[0]).intersection(roots[1])
            tests += 1
    return tests


def class_tests():
    p = 13
    mod = p*p
    results = {}
    for xy in [(0,0),(1,0),(5,1),(3,4)]:
        good = prim = 0
        for i,j in product(range(p),repeat=2):
            x,y = xy[0]+p*i,xy[1]+p*j
            a,b = norms(x,y)
            prim += bool(x%p or y%p)
            good += bool(a%mod and b%mod)
        label = ','.join(map(str,xy))
        expected = 0 if not prim else (p*(p-1) if 0 in [z%p for z in norms(*xy)] else p*p)
        assert good == expected
        results[label] = [good,prim]
    return results


def square_table(limit):
    # square root of largest square divisor, via all squares (including composites)
    table = [1]*(limit+1)
    for h in range(2,isqrt(limit)+1):
        for n in range(h*h,limit+1,h*h):
            table[n] = h
    return table


def samples():
    limit = 224
    sq = square_table(3*limit**2)
    profiles = {k:Counter() for k in ('box','positive_sector_x_ge_2y','negative_sector_x_ge_-2y',
                                       'box_x=5_y=1_mod13','box_x=70_y=1_mod169')}
    for x,y in product(range(-limit,limit+1), repeat=2):
        if not (x or y):
            continue
        a,b = norms(x,y)
        u,v = sq[a],sq[b]
        g = gcd(x,y)
        assert gcd(a,b) == g*g and gcd(u,v) == g
        labels = ['box']
        if x>=2*y>0: labels.append('positive_sector_x_ge_2y')
        if x>=-2*y>0: labels.append('negative_sector_x_ge_-2y')
        if (x%13,y%13)==(5,1): labels.append('box_x=5_y=1_mod13')
        if (x%169,y%169)==(70,1): labels.append('box_x=70_y=1_mod169')
        for name in labels:
            d = profiles[name]
            d['all'] += 1
            if g!=1: continue
            d['primitive'] += 1
            d['N_squarefree'] += u==1
            d['C_squarefree'] += v==1
            d['both_squarefree'] += u==v==1
            d['square_parts_5_7'] += (u,v)==(5,7)
    return {'coordinate_bound':limit,'counts':{k:dict(v) for k,v in profiles.items()}}


def shear_control():
    p,m = 13,169
    a,b = root_lists(p)
    counts = [sum((x+t)%m in b for x in a) for t in range(m)]
    assert sum(counts)==4 and counts[48]==1
    whole = sum(all(z%m for z in norms(x,y,48))
                for x,y in product(range(m),repeat=2))
    assert whole == (m*(m-1)) * F(179,182)
    r13 = F(179*182,180**2)
    assert r13 == F(16289,16200)
    tail = F(4,36**4) + F(4,3*36**3)
    assert r13*(1-tail)>1
    return {'p13_roots_N_and_C': [a,b], 'p13_h_by_shear_histogram': sorted(Counter(counts).items()),
            't48_mod169_both_squarefree_at13':whole,'t48_ratio_factor_p13':str(r13),
            'certified_ratio_lower_t48':str(r13*(1-tail))}


def frame_witnesses():
    # Finite witnesses from independent integral-matrix search; test using raw coordinates.
    matrices = [
        (0,1,-1,1),(12,-23,-13,25),(15,-28,-23,43),
        (2,-3,-7,11),(11,-626,-12,683),(10,80203,-27,-216548),
        (15,4,-124,-33),(136,20325,-165,-24659),(117886,164303,-34883,-48618)]
    hits = {}
    for i,(a,b,c,d) in enumerate(matrices+[(3,7,-4,-9)]):
        assert a*d-b*c == 1
        first = norms(a,c)[1]
        last = norms(b,d)[1]
        middle = norms(a+b,c+d)[1]-first-last
        res = (first+last)**2-3
        assert res == (first-last)**2+middle**2
        roots = []
        for p in (13,37):
            mod = p*p
            same = [r for r in range(mod) if (r*r+1)%mod==0
                    and norms(a*r+b,c*r+d)[1]%mod==0]
            assert not same or res % mod == 0
            roots.append(same)
        if i < 9:
            assert tuple(map(len,roots))==divmod(i,3)
        else:
            assert res==52897 and res%(13*13)==0 and not roots[0]
        hits[f'{a},{b},{c},{d}']=roots
    return hits


def capped_square_parts():
    # One modulus contains both p^2 and p^4; compare exact and tail exponent frequencies.
    p=5
    mod=p**4
    histogram=Counter()
    for x,y in product(range(mod),repeat=2):
        if x%p or y%p:
            n=x*x+y*y
            histogram[(n%(p*p)==0)+(n%mod==0)]+=1
    total=mod**2-(mod//p)**2
    assert F(histogram[1],total)==F(2*(p-1),p**3)
    assert F(histogram[2],total)==F(2,p**3*(p+1))
    return list(map(histogram.__getitem__,range(3)))


def interval(lo,hi):
    """Integers bounding the requested number in units of 10^-12."""
    s = 10**12
    return [s*lo.numerator//lo.denominator,-((-s*hi.numerator)//hi.denominator)]


def constants():
    B=4000
    dens = [F(1),F(1),F(1)]
    ratio = F(1)
    avg = F(1)
    for p in primes_to(B):
        den = p*(p+1)
        a = 2*int(p%4==1)
        b = 2*int(p%3==1)
        for i,v in enumerate((a,b,a+b)):
            dens[i] *= F(den-v,den)
        if a and b:
            ratio *= 1-F(4,(den-2)**2)
            avg *= 1+F(4,p*(den-2)**2)
    # For n>B, (n-1)^-4 summed by first term and decreasing tail integral.
    tail4 = 4*(F(1,B**4)+F(1,3*B**3))
    # prod(1+x) <= 1/(1-sum(x)) for nonnegative x of total <1.
    return {'prime_cutoff':B,'units':'10^-12; inclusive endpoints',
            'primitive_N_C_joint':[interval(d*(1-F(c,B+1)),d) for d,c in zip(dens,(2,2,4))],
            'identity_ratio':interval(ratio*(1-tail4),ratio),
            'mean_shear_ratio':interval(avg,avg/(1-tail4/B))}


def three_intervals():
    common = [p for p in primes_to(2_000) if p%12==1]
    tests = []
    for p in common:
        if 37 <= p < 1_000:
            dyad = [ell for ell in common if p<ell<=2*p]
            ratio = (p*(p+1)-4)*sum(F(2,ell*(ell+1)-2) for ell in dyad)
            assert ratio>1
            tests.append((ratio,p,dyad))
    ratio,p,dyad=min(tests)
    assert len(tests)==35 and ratio==F(11917,9450) and dyad==[61,73]
    first_tail = (F(1,9)+F(1,25)+F(1,5))/72
    assert first_tail==F(79,16200)<F(1,180)
    return {'finite_comparisons':len(tests),'minimum_ratio':str(ratio),'at_prime':p,
            'following_dyad_primes':dyad,'tail_after_13_upper':str(first_tail),
            'smaller_gap_at_13_lower':'1/180','closed_interval_components':3}


def tight_joint_constant():
    cutoff = 12_000_000
    scale = 10**27
    lower = upper = scale
    mask = prime_mask(cutoff)
    for p in range(5,cutoff+1,2):
        if not mask[p]:
            continue
        roots = 2*(int(p%4==1)+int(p%3==1))
        if roots:
            denominator = p*(p+1)
            numerator = denominator-roots
            lower = lower*numerator//denominator
            upper = (upper*numerator+denominator-1)//denominator
    # The product of (1-loss) dominates 1 minus the sum of all tail losses.
    lower = lower*(cutoff-3)//(cutoff+1)
    digits = interval(F(lower,scale),F(upper,scale))
    assert digits == [855395415914,855395701047]
    return {'prime_cutoff':cutoff,'integer_rounding_grid':str(scale),
            'units':'10^-12; inclusive endpoints','primitive_joint':digits}


def main():
    ps=(2,3,5,7,11,13,17,19)
    print(json.dumps({'valuation_root_checks':valuation_tests(), 'primitive_p2_grids':{p:local_grid(p) for p in ps},
                      'mod13_class_good_and_primitive':class_tests(),'shear':shear_control(),
                      'GL2_common_roots_13_37':frame_witnesses(),'capped_5_squarepart_counts':capped_square_parts(),
                      'empirical':samples(),'constant_bounds':constants(),
                      'tight_joint_constant':tight_joint_constant(),'three_intervals':three_intervals()},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
