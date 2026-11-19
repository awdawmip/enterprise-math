"""Exact Gaussian valuation and principal-sheet search. Python 3.10+, standard library."""
import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
from typing import NamedTuple

SCALE = 1000
CAP = 1694
TEN = 10**SCALE
BOX_SWITCH = 9


def mul(z, w):
    x, y = z
    a, b = w
    return x*a-y*b, x*b+y*a


def div(z, w):
    x, y = mul(z, (w[0], -w[1]))
    n = w[0]**2+w[1]**2
    if x % n or y % n:
        return None
    return x//n, y//n


@cache
def split(p):
    for y in range(1, math.isqrt(p)+1):
        x = math.isqrt(p-y*y)
        if x >= y and x*x+y*y == p:
            return x, y
    raise ValueError(p)


def factor(n):
    p = 2
    while p*p <= n:
        if n % p == 0:
            yield p
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p+2
    if n > 1:
        yield n


class Atom(NamedTuple):
    b: int
    a: int
    q: int
    torsion: int
    v: dict


@cache
def atom(b, a):
    z, e, v = (b, a), 0, {}
    for p in factor(b*b+a*a):
        if p == 2:
            z = div(z, (1, 1))
            e = 1
            continue
        x, y = split(p)
        v[p] = 0
        for sign in (1, -1):
            while (w := div(z, (x, sign*y))) is not None:
                z = w
                v[p] += sign
        assert v[p]
    units = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return Atom(b, a, floorcost(b, a), (e+2*units.index(z)) % 8, v)


@cache
def floorcost(b, a):
    q = int(SCALE/math.log10(b/a))
    while b**q > TEN*a**q:
        q -= 1
    while b**(q+1) <= TEN*a**(q+1):
        q += 1
    return q


def at_most(b, a, q):
    # Decide floor(cost) <= q without evaluating very large costs near slope 1.
    if q < 0:
        return False
    return b**(q+1) > TEN*a**(q+1)


def ranges(j, cap):
    for b in range(1 << (j-1), 1 << j):
        for a in range(1, b):
            if not at_most(b, a, cap):
                break
            if math.gcd(a, b) == 1:
                yield atom(b, a)


def determinant(v, w, i, j):
    return v.get(i, 0)*w.get(j, 0) - v.get(j, 0)*w.get(i, 0)


@cache
def prime_exp(p, exponent):
    x, y = split(p)
    base, z, h = (x, (1 if exponent >= 0 else -1)*y), (1, 0), abs(exponent)
    while h:
        if h & 1:
            z = mul(z, base)
        base = mul(base, base)
        h //= 2
    return z


def rebuild(v):
    z = (1, 0)
    for p, exponent in v.items():
        z = mul(z, prime_exp(p, exponent))
    for candidate in [z, mul(z, (1, 1))]:
        for _ in range(4):
            b, a = candidate
            if 0 < a < b:
                return b, a
            candidate = (-a, b)
    if v:
        raise AssertionError(v)


@cache
def max_exponent(p, norm):
    h = 0
    while norm >= p:
        norm //= p
        h += 1
    return h


def line_vectors(v, norm):
    g = math.gcd(*v.values())
    base = {p: t//g for p, t in v.items()}
    mass = math.prod(p**abs(t) for p, t in base.items())
    h = max_exponent(mass, norm)
    for n in range(-h, h+1):
        if n:
            yield {p: n*t for p, t in base.items()}


def pivot_lattice(v, w, i, j):
    """Image of the saturated plane, in column-Hermite coordinates."""
    axes = sorted(v.keys() | w.keys())
    d = abs(determinant(v,w,i,j))
    index0 = math.gcd(*(determinant(v,w,p,r) for p,r in combinations(axes,2)))
    conditions = [(w.get(j,0)*v.get(p,0)-v.get(j,0)*w.get(p,0),
                   v.get(i,0)*w.get(p,0)-w.get(i,0)*v.get(p,0)) for p in axes]
    stride_t = math.lcm(*(d//math.gcd(b,d) for a,b in conditions))
    stride_s = (d//index0)//stride_t
    value, modulus = 0, 1
    for a,b in conditions:
        g=math.gcd(b,d)
        assert a*stride_s % g==0
        new_mod=d//g
        residue=(-a*stride_s//g)*pow(b//g,-1,new_mod)%new_mod
        common=math.gcd(modulus,new_mod)
        assert (residue-value)%common==0
        quotient=new_mod//common
        step=(residue-value)//common*pow(modulus//common,-1,quotient)%quotient
        value+=modulus*step
        modulus*=quotient
    assert modulus==stride_t and stride_s*stride_t==d//index0
    return stride_s,value%stride_t,stride_t


def planes(v, w, width):
    norm = 2*((1 << width)-1)**2
    axes = sorted(v.keys() | w.keys())
    pivots = [(i, j) for i, j in combinations(axes, 2) if determinant(v, w, i, j)]
    if not pivots:
        yield from line_vectors(v, norm)
        return
    i, j = min(pivots, key=lambda ij: math.prod(2*max_exponent(h, norm)+1 for h in ij))
    d = determinant(v, w, i, j)
    m, n = max_exponent(i, norm), max_exponent(j, norm)
    coords = [(p, v.get(p, 0), w.get(p, 0)) for p in axes]
    stride_s, offset, stride_t = pivot_lattice(v,w,i,j)
    for s in range(-(m//stride_s)*stride_s, m+1, stride_s):
        t0 = -n+(offset*(s//stride_s)+n)%stride_t
        for t in range(t0, n+1, stride_t):
            l = w.get(j, 0)*s-w.get(i, 0)*t
            r = v.get(i, 0)*t-v.get(j, 0)*s
            if l == 0 or r == 0:
                # Only a relation with a vanishing coefficient could use this line.
                continue
            out, mass = {}, 1
            for p, x, y in coords:
                value, rem = divmod(l*x+r*y, d)
                if rem:
                    break
                if value:
                    if abs(value) > max_exponent(p, norm):
                        break
                    mass *= p**abs(value)
                    if mass > norm:
                        break
                    out[p] = value
            else:
                yield out


def winding(zs, cs):
    z, turn, crossings = (1, 0), 0, 0
    for u, c in zip(zs, cs):
        for _ in range(abs(c)):
            w = mul(z, (u.b, u.a if c > 0 else -u.a))
            g = math.gcd(*w)
            w = w[0]//g, w[1]//g
            if z[0] > 0 and w[0] > 0 and (z[1] < 0) != (w[1] < 0):
                turn += 1 if z[1] < 0 else -1
                crossings += 1
            z = w
    return z, turn, crossings


def classify(zs):
    v, w, z = [a.v for a in zs]
    axes = sorted(v.keys() | w.keys() | z.keys())
    for i, j in combinations(axes, 2):
        d = determinant(v, w, i, j)
        if d:
            break
    else:
        if all(determinant(v, z, i, j) == 0 for i, j in combinations(axes, 2)):
            return 'rank_one', None
        return 'nonminimal', None
    coeff = (determinant(w, z, i, j), determinant(z, v, i, j), d)
    if any(sum(c*a.v.get(p, 0) for c, a in zip(coeff, zs)) for p in axes):
        return 'rank_three', None
    if not all(coeff):
        return 'nonminimal', None
    g = math.gcd(*coeff)
    coeff = [c//g for c in coeff]
    e = sum(c*a.torsion for c, a in zip(coeff, zs)) % 8
    if e % 2 == 0:
        return 'even', None
    multiple = e if e < 4 else e-8
    return 'odd', [c*multiple for c in coeff]


def logarithm(x):
    k, power2 = 0, Fraction(1)
    while x >= 2*power2:
        k += 1
        power2 *= 2
    def segment(y):
        v = (y-1)/(y+1)
        acc, power = Fraction(0), v
        for j in range(36):
            acc += 2*power/(2*j+1)
            power *= v*v
        return acc, acc+2*power/((2*36+1)*(1-v*v))
    return tuple(a+k*b for a, b in zip(segment(x/power2), segment(Fraction(2))))


@cache
def analytic(b, a):
    lower, upper = logarithm(Fraction(b, a))
    lo, hi = logarithm(Fraction(10))
    return lo/upper, hi/lower


def witness(zs, cs):
    endpoint, turn, crossings = winding(zs, cs)
    assert endpoint == (1, 1)
    bounds = [sum(analytic(u.b, u.a)[j] for u in zs)*10**12 for j in (0, 1)]
    return dict(slopes=[[u.a,u.b] for u in zs], coeff=cs, endpoint=list(endpoint),
                winding=turn, crossings=crossings, l1=sum(map(abs,cs)),
                max_b=max(u.b for u in zs), bits=sum(u.b.bit_length() for u in zs),
                mu_scaled_bounds=[math.floor(bounds[0]),math.ceil(bounds[1])])


def box_choices(index, v, w):
    a, b = v.keys(), w.keys()
    must, shared = a ^ b, sorted(a & b)
    for size in range(len(shared)+1):
        for subset in combinations(shared, size):
            yield from index.get(frozenset(must.union(subset)), ())


def affine_choices(x, y, f, cap):
    for v in planes(x.v, y.v, f):
        b, a = rebuild(v)
        if b.bit_length() == f and (b, a) > (y.b, y.a) and at_most(b, a, cap):
            z = atom(b, a)
            assert z.v == v
            yield z


def plane_key(v, w):
    axes = sorted(v.keys() | w.keys())
    minors = [(i,j,determinant(v,w,i,j)) for i,j in combinations(axes,2)]
    minors = [(i,j,t) for i,j,t in minors if t]
    g = math.gcd(*(t for i,j,t in minors))*(1 if minors[0][2] > 0 else -1)
    return tuple((i,j,t//g) for i,j,t in minors)


def count_universe(caps):
    u = 2**max(caps)-1
    mu = [1]*(u+1)
    composite = bytearray(u+1)
    for p in range(2,u+1):
        if composite[p]:
            continue
        for k in range(p,u+1,p):
            composite[k]=1
            mu[k] *= -1
        for k in range(p*p,u+1,p*p):
            mu[k]=0
    answer = {}
    for j, q in sorted(caps.items()):
        denominator = 2**40
        m = int(denominator*10.0**(-SCALE/(q+1)))
        target = denominator**(q+1)
        while TEN*m**(q+1)>target:
            m -= 1
        while TEN*(m+1)**(q+1)<=target:
            m += 1
        max_b=2**j-1
        low_b=2**(j-1)
        top=[0]*(max_b+1)
        for b in range(low_b,max_b+1):
            a=m*b//denominator
            while a and not at_most(b,a,q):
                a-=1
            ceiling=((m+1)*b-1)//denominator
            while a<ceiling and at_most(b,a+1,q):
                a+=1
            top[b]=a
        answer[str(j)] = sum(mu[d]*sum(top[b]//d for b in range(((low_b+d-1)//d)*d,max_b+1,d))
                             for d in range(1,max_b+1) if mu[d])
    return answer


def bit_search(all_support=False):
    costs = {j: floorcost(2**j-1, 1) for j in range(2, 21)}
    pats = [pat for pat in combinations_with_replacement(costs,3)
            if 22 <= sum(pat) <= 24 and sum(costs[j] for j in pat) <= CAP]
    caps, all_caps = defaultdict(int), defaultdict(int)
    for d,e,f in pats:
        for h in (d,e,f):
            all_caps[h] = max(all_caps[h],CAP-costs[d]-costs[e]-costs[f]+costs[h])
        for h in ((d,e,f) if (all_support or f<=BOX_SWITCH) else (d,e)):
            caps[h] = max(caps[h], CAP-costs[d]-costs[e]-costs[f]+costs[h])
    small = {j:list(ranges(j,cap)) for j, cap in sorted(caps.items())}
    counts, hits, packs = defaultdict(Counter), [], {}
    plane_sets = defaultdict(set)
    for d,e,f in pats:
        key = (d,e,f)
        capx, capy = CAP-costs[e]-costs[f], CAP-costs[d]-costs[f]
        xs, ys = [u for u in small[d] if u.q <= capx], [u for u in small[e] if u.q <= capy]
        index = defaultdict(list)
        if (all_support or f<=BOX_SWITCH):
            for u in small[f]:
                if u.q<=CAP-costs[d]-costs[e]:
                    index[frozenset(u.v)].append(u)
        pair_count, exact_cases, digest = 0, 0, hashlib.sha256()
        for x in xs:
            for y in ys:
                capz=CAP-x.q-y.q
                if (x.b,x.a)>=(y.b,y.a) or capz<costs[f]:
                    continue
                pair_count+=1
                choices=(box_choices(index,x.v,y.v) if (all_support or f<=BOX_SWITCH) else affine_choices(x,y,f,capz))
                for z in choices:
                    if (y.b,y.a)>=(z.b,z.a) or z.q>capz:
                        continue
                    zs=(x,y,z)
                    kind,coeff=classify(zs)
                    if all_support and kind in ('rank_three','nonminimal'):
                        counts[sum(key)][kind]+=1
                    if kind in ('even','odd'):
                        plane_sets[sum(key)].add(plane_key(x.v,y.v))
                    if kind in ('rank_one','even','odd'):
                        exact_cases+=1
                        digest.update((str([(u.b,u.a) for u in zs])+kind+'\n').encode())
                        counts[sum(key)][kind]+=1
                        if sum(u.q for u in zs)<=1552:
                            counts[sum(key)]['tight_'+kind]+=1
                    if kind=='rank_one':
                        raise AssertionError(('material rank-one case requires full kernel',zs))
                    if kind=='odd':
                        hits.append(witness(zs,coeff))
        packs['/'.join(map(str,key))] = [pair_count,exact_cases,digest.hexdigest()[:24]]
    return dict(cap=CAP,box_switch=BOX_SWITCH,widths=packs,
                ramified_and_unit_choices_checked=True,
                all_screened_alphabet_counts=count_universe(all_caps),
                occupied_circuit_planes={str(k):len(v) for k,v in plane_sets.items()},
                first_two_box_atom_counts={str(j):len(arr) for j,arr in small.items()},
                counts={str(b):dict(sorted(c.items())) for b,c in sorted(counts.items())},
                hits=sorted(hits,key=lambda hit: (hit['bits'], hit['slopes'])))


def beyond_million():
    out, all_odd = Counter(), Counter()
    hits = []
    for b in range(2,16):
        for a in range(1,b):
            if math.gcd(b,a)!=1:
                continue
            x=atom(b,a)
            out['small_atoms']+=1
            cap=24-b.bit_length()
            for v in line_vectors(x.v, 2*((1<<cap)-1)**2):
                d,c=rebuild(v)
                if d<=10**6 or d.bit_length()>cap:
                    continue
                out['large_collinear_pairs']+=1
                z=atom(d,c)
                passes=at_most(d,c,1552-x.q)
                if passes:
                    out['large_pairs_through_cost_screen']+=1
                p=next(iter(x.v))
                g=math.gcd(v[p],x.v[p])
                co=[v[p]//g,-x.v[p]//g]
                e=sum(u.torsion*t for u,t in zip((x,z),co))%8
                if e%2:
                    all_odd[b.bit_length()+d.bit_length()]+=1
                    if not passes:
                        continue
                    hits.append(witness([x,z],[t*(e if e<4 else e-8) for t in co]))
    return dict(counts=dict(out),large_odd_counts_by_exact_bits=dict(sorted(all_odd.items())),candidates=hits)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    parser.add_argument('--all-support',action='store_true',help='independent slower enumeration of every supported third column')
    args=parser.parse_args()
    result=dict(support_three=bit_search(args.all_support), two_large=beyond_million(),
                hnf_example=pivot_lattice(atom(11,3).v,atom(33,4).v,5,13),
                benchmarks=[witness([atom(57,1),atom(79,3),atom(239,1)],[20,12,-5]),
                            witness([atom(79,3),atom(22049,1457)],[12,5])])
    doc=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(doc)
    else:
        print(doc,end='')

if __name__=='__main__':
    main()
