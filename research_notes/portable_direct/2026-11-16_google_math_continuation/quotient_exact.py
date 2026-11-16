"""Sharp phase thresholds under common additive offset using exact rational comparisons.

Every signature is the residue P sampled at J. All Y and P numbers are scaled
by 108. The quotient distance is half the range of the coordinatewise residual.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from bisect import bisect_left
import json
import sys

P = tuple(3 * x for x in (455, -295, -25, 185, -25, -295))
ERRORS = tuple(range(-2, 3))
TRIP = (0, 1, 5)
PAIRS = ((0, 1), (0, 5))
BUDGET = 2
SOURCES = (1,1,2,3,6)
TOP = 8005

# coefficients counting all labelled histories of cost <= q-1, including slack.
c = [1] + [0]*TOP
for w in (1, *SOURCES):
    for j in range(w, TOP + 1):
        c[j] += c[j-w]
# multiplying count series by t/(1-t) marks total multiplicity of first source.
C = [0]+c
T = [0]*(len(C))
for q in range(1, len(C)):
    T[q] = T[q-1]+C[q-1]

@lru_cache(maxsize=150)
def readings(q):
    s = 18*q**4+54*q**3-345*q*q+2070*q-16315
    return {(e,d): Fraction(108*q**3*(T[q]+e), C[q]+d)-s
            for e in ERRORS for d in ERRORS if C[q]+d>0}

@lru_cache(maxsize=1500)
def possibilities(q, e, d):
    vals = readings(q)
    return sorted((v,E,D) for (E,D),v in vals.items()
                  if (e is None or E==e) and (d is None or D==d))

def shared_options(part, k):
    if part is True:
        indices = tuple(range(k))
    elif part is False:
        indices = ()
    else:
        indices = tuple(part)
    if not indices:
        return [(None,)*k]
    return [tuple(v if i in indices else None for i in range(k)) for v in ERRORS]

def failure(r, J, ec, dc):
    """At fixed common biases, all remaining coordinates vary independently."""
    sigs = [tuple(P[(a+j)%6] for j in J) for a in range(6)]
    a = r % 6
    A = sigs[a]
    competitors = [S for k,S in enumerate(sigs) if k != a]
    def drange(v):
        return max(v) - min(v)
    margin = min(drange([x-y for x,y in zip(A,B)]) for B in competitors)
    maxhi = [possibilities(r+j,None,None)[-1][0]-p for j,p in zip(J,A)]
    minlo = [possibilities(r+j,None,None)[0][0]-p for j,p in zip(J,A)]
    if 2 * (max(maxhi)-min(minlo)) < margin:
        return None
    if len(J)==2:
        for es,ds in product(shared_options(ec,len(J)),shared_options(dc,len(J))):
            vals=[possibilities(r+j,e,d) for j,e,d in zip(J,es,ds)]
            if not all(vals):
                continue
            for x,y in ((vals[0][0],vals[1][-1]),(vals[0][-1],vals[1][0])):
                diff=y[0]-x[0]
                d1=abs(diff-A[1]+A[0])
                nearest = min((abs(diff-B[1]+B[0]), b) for b,B in enumerate(sigs) if b!=a)
                if nearest[0]<=d1:
                    return dict(r=r,a=a,b=nearest[1],error=[x[1:],y[1:]],
                                true_quotient_distance=str(d1/216),rival_quotient_distance=str(nearest[0]/216))
        return None
    for es,ds in product(shared_options(ec,len(J)),shared_options(dc,len(J))):
        cols = [possibilities(r+j,e,d) for j,e,d in zip(J,es,ds)]
        if any(not arr for arr in cols):
            continue
        lo,hi = [arr[0] for arr in cols], [arr[-1] for arr in cols]
        for b,B in enumerate(sigs):
            if b == a:
                continue
            # For this rival the ideal spread is range(S_a - S_b).
            H = max(x-y for x,y in zip(A,B))-min(x-y for x,y in zip(A,B))
            range_bound = max(x[0]-s for x,s in zip(hi,A))-min(x[0]-s for x,s in zip(lo,A))
            if 2*range_bound < H:
                continue
            # If a rival ties/beats, one ordered pair realizes true spread.
            # Its left residual increases when y_i grows or y_j falls,
            # at least as much as every directed difference of the rival.
            for i,j in permutations(range(len(J)),2):
                sample = [None]*len(J)
                sample[i],sample[j] = hi[i],lo[j]
                true_edge = hi[i][0]-lo[j][0]-A[i]+A[j]
                ri,rj = hi[i][0]-B[i],lo[j][0]-B[j]
                if true_edge < abs(ri-rj):
                    continue
                free = [k for k in range(len(J)) if k not in (i,j)]
                if free:
                    # All residuals must span at most true_edge. For k remaining
                    # this means a closed interval; use a sorted *discrete* list.
                    k, = free
                    low = max(ri,rj)-true_edge+B[k]
                    upper = min(ri,rj)+true_edge+B[k]
                    pos = bisect_left(cols[k], (low,))
                    if pos == len(cols[k]) or cols[k][pos][0] > upper:
                        continue
                    sample[k] = cols[k][pos]
                def spread(S):
                    vals=[item[0]-s for item,s in zip(sample,S)]
                    return max(vals)-min(vals)
                x,y=spread(A),spread(B)
                assert x>=y
                return dict(r=r,a=a,b=b,error=[item[1:] for item in sample],
                            true_quotient_distance=str(x/216),rival_quotient_distance=str(y/216))
    return None

def envelope(q):
    return Fraction(1600,q) + (Fraction(4320,q*q)*(2+2*(Fraction(q,6)+1)))/(1-Fraction(8640,q**5))

def run():
    J=tuple(map(int,sys.argv[1].split(',')))
    tail=1350 if len(J)==3 else 8000
    dist=Fraction(20,3) if len(J)==3 else Fraction(5,6)
    assert envelope(tail) < dist/2
    modes=[(True,True),(False,True),(True,False),(False,False)]
    if len(sys.argv)>2:
        modes=[modes[int(sys.argv[2])]]
    for ec,dc in modes:
        for r in range(tail-1,0,-1):
            w=failure(r,J,ec,dc)
            if w:
                print(json.dumps(dict(J=J,ec=ec,dc=dc,threshold=r+1,tail=tail,witness=w)),flush=True)
                break

if __name__ == '__main__':
    run()
