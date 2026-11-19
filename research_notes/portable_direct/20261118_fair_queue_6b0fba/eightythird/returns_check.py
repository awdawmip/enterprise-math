"""Finite graded counts of identity histories under two native path quotients."""
import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha1
from itertools import product
import json
from math import comb, isqrt
from pathlib import Path
import runpy

LETTERS = tuple(j for i in range(1, 7) for j in (i, -i))
SOURCE = "experiments/x6_rotation_path_dagger_jet_20260909/check_rotation_path_dagger_jet.py"
SOURCE_BLOB = "51a567303d2d6da37c82dda418b82c5d90a1e4a9"


def source_check(repo):
    file = repo / SOURCE
    data = file.read_bytes()
    actual = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    assert actual == SOURCE_BLOB
    api = runpy.run_path(str(file))
    def decode(w):
        return tuple((1 + axis) * sign for axis, sign in map(api["step_letter"], w))
    result = []
    for i, start in enumerate(api["ORBIT"]):
        end = api["ORBIT"][(i + 1) % 6]
        for branch in (False, True):
            w = api["edge_steps"](start, end, branch)
            actual = decode(w)
            assert decode(api["reverse_steps"](w)) == invert(actual)
            result.append(actual)
    assert len(set(result)) == 12
    return {"source_blob": SOURCE_BLOB, "all_native_signed_macro_lifts": result}


def invert(w):
    return tuple(-z for z in reversed(w))


def first_returns(n):
    """Dimension recurrence: insert 2j steps on the last labelled axis."""
    c = [1] + [0] * n
    for _ in range(6):
        c = [sum(comb(2*i, 2*j) * comb(2*j, j) * c[i-j] for j in range(i+1))
             for i in range(n+1)]
    f = [0]
    for i in range(1, n+1):
        f.append(c[i] - sum(f[j]*c[i-j] for j in range(1, i)))
    return c, f


def cavity(f):
    """First returns launched by one specified symbol of half-length k."""
    n = len(f) - 1
    h = [[0]*(n+1) for _ in range(n+1)]
    outgoing = [0]*(n+1)
    d = [1] + [0]*n
    for t in range(1, n+1):
        for k in range(1, t+1):
            h[k][t] = int(k == t) + sum(
                h[k][s] * (outgoing[t-s] - h[k][t-s]) for s in range(k,t))
        outgoing[t] = sum(f[k]*h[k][t] for k in range(1, t+1))
        d[t] = sum(outgoing[s]*d[t-s] for s in range(1, t+1))
    return d


def verify_scalar(d, f):
    """Use the integer Catalan expansion of each square root."""
    n = len(d) - 1
    p = [1] + [0]*n
    v = [1] + [0]*n
    for j in range(1, n+1):
        for _ in range(2):
            p = [sum(p[h]*d[t-h] for h in range(t+1)) for t in range(n+1)]
        multiplier = (-1)**(j-1) * (comb(2*j-2,j-1)//j)
        for t in range(j,n+1):
            v[t] += multiplier * sum(f[k]*p[t-j*k] for k in range(1,t//j+1))
    assert v == d


def complements(f, d, depth=8):
    def times(a, b):
        return [sum(a[i]*b[t-i] for i in range(t+1)) for t in range(depth+1)]
    d = d[:depth+1]
    squared = times(d,d)
    odd_power = d
    deriv = [0]*(depth+1)
    for h in range(1,depth+1):
        factor = (-1)**(h-1)*2*comb(2*h-2,h-1)
        for t in range(h,depth+1):
            deriv[t] += factor * sum(f[k]*odd_power[t-h*k] for k in range(1,t//h+1))
        odd_power = times(odd_power,squared)
    K = []
    for t in range(depth+1):
        K.append(squared[t]+sum(deriv[t-i]*K[i] for i in range(t)))
    # Insert a fresh symbol at two distinct lengths. At these orders it occurs in only one pair.
    for giant in (11,15):
        amended = f[:giant+depth+1]
        ordinary = cavity(amended)
        amended[giant] += 1
        extra = cavity(amended)
        assert [extra[giant+j]-ordinary[giant+j] for j in range(depth+1)] == K
    # Second independent test label. Mixed inclusion/exclusion isolates the two marked pairs.
    second = [0]*(depth+1)
    even_power = [1]+[0]*depth
    for h in range(1,depth+1):
        factor = (-1)**(h-1)*2*(2*h-1)*comb(2*h-2,h-1)
        for t in range(h,depth+1):
            second[t] += factor*sum(f[k]*even_power[t-h*k] for k in range(1,t//h+1))
        even_power = times(even_power,squared)
    dK = times(d,K)
    secondKK = times(second,times(K,K))
    K2 = []
    for t in range(depth+1):
        K2.append(secondKK[t]+4*dK[t]+sum(deriv[t-i]*K2[i] for i in range(t)))
    both = []
    for mask in range(4):
        amended = f[:27+depth]
        amended[11] += mask & 1
        amended[15] += mask >> 1
        both.append(cavity(amended)[26:])
    assert [a-b-c+e for a,b,c,e in zip(*both)] == K2
    return {"one_mark":K,"two_distinct_marks":K2}


def primitive(pairs):
    # Heights in the regular 12-tree; a downstep is forced.
    state = [1]
    for _ in range(2*pairs):
        future = [0]*(len(state)+1)
        for h,v in enumerate(state):
            future[h+1] += (12 if h == 0 else 11)*v
            if h:
                future[h-1] += v
        state = future
    return state[0]


def ends(w):
    z = [0]*6
    for s in w:
        z[abs(s)-1] += 1 if s > 0 else -1
    return tuple(z)


def reductions(w):
    z = [0]*6
    primitive_stack = []
    excursion_stack = []
    start = 0
    for i,s in enumerate(w, 1):
        z[abs(s)-1] += 1 if s > 0 else -1
        if primitive_stack and primitive_stack[-1] == -s:
            primitive_stack.pop()
        else:
            primitive_stack.append(s)
        if not any(z):
            ex = w[start:i]
            if excursion_stack and excursion_stack[-1] == invert(ex):
                excursion_stack.pop()
            else:
                excursion_stack.append(ex)
            start = i
    assert start == len(w)
    return not excursion_stack, not primitive_stack


def enumerate_closed(half):
    # Two halfwords reaching the same endpoint form w followed by v^dagger.
    groups = defaultdict(list)
    for w in product(LETTERS, repeat=half):
        groups[ends(w)].append(w)
    nclosed = nrotation = nprimitive = 0
    for words in groups.values():
        backward = [invert(v) for v in words]
        for w in words:
            for b in backward:
                rot, prim = reductions(w+b)
                assert not rot or prim
                nclosed += 1
                nrotation += rot
                nprimitive += prim
    return [nclosed, nrotation, nprimitive]


def sqrt_bounds(x, scale=10**15):
    v = isqrt((x.numerator*scale**2)//x.denominator)
    return Fraction(v,scale), Fraction(v+1,scale)


def endpoints(c, f):
    """Outward bounds at u=1/144; store reproducible integral millionth units."""
    N = len(c)-1
    a = sum(Fraction(v,144**i) for i,v in enumerate(c))
    a_hi = a + Fraction(5,3*N*N)
    alpha8 = sum(Fraction(c[i],144**i) for i in range(1,9)) + Fraction(5,3*8*8)
    assert alpha8 < Fraction(1,4)
    weights = [Fraction(f[k],144**k) for k in range(1,N+1)]
    residual = 1 - 1/a_hi - sum(weights)
    def bounding(y, derivative):
        out_lo = out_hi = Fraction(0)
        for k,r in enumerate(weights,1):
            l,h = sqrt_bounds(1+4*y*y/Fraction(144**k))
            if derivative:
                out_lo += 2*y*r/h
                out_hi += 2*y*r/l
            else:
                out_lo += 2*y*y*r/(1+h)
                out_hi += 2*y*y*r/(1+l)
        return out_lo, out_hi+residual*(2*y if derivative else y*y)
    def bisect(upper):
        l,h = Fraction(1),Fraction(2)
        for _ in range(32):
            mid = (l+h)/2
            val = bounding(mid,False)[int(upper)]
            if 1+val >= mid: l = mid
            else: h = mid
        return h if upper else l
    dlo,dhi = bisect(False),bisect(True)
    vlo = bounding(dlo,True)[0]
    vhi = bounding(dhi,True)[1]
    assert vhi < 1
    def denoise(lo,hi):
        scale = 10**6
        return [lo.numerator*scale//lo.denominator,
                -(-hi.numerator*scale//hi.denominator)]
    return {"rounding_scale":10**6,
            "G":denoise(a,a_hi), "D":denoise(dlo,dhi),
            "asymptotic_ratio_Dn_over_first_return_2n":
                denoise(dlo**2/(1-vlo),dhi**2/(1-vhi)),
            "alpha_bound_from_eight_terms":denoise(alpha8,alpha8)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--out",type=Path)
    opts = parser.parse_args()
    c,f = first_returns(64)
    d = cavity(f)
    verify_scalar(d,f)
    p = [primitive(2*n) for n in range(len(f))]
    brute = {half:enumerate_closed(half) for half in range(5)}
    for h,(closed,rot,prim) in brute.items():
        assert (closed,rot,prim) == (c[h], d[h//2] if h%2 == 0 else 0, primitive(h))
    result = {"source":source_check(opts.repo),"brute_by_half_length_closed_rot_primitive":brute,
              "rows_n_f2n_D4n_primitive4n":[[n,f[n],d[n],p[n]] for n in range(len(d))],
              "marked_complement_coefficients":complements(f,d),
              "critical":endpoints(c,f)}
    result = json.dumps(result,sort_keys=True,indent=2) + "\n"
    if opts.out: opts.out.write_text(result)
    else: print(result,end="")


if __name__ == "__main__":
    main()
