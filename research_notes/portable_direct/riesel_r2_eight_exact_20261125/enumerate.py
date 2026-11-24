from itertools import combinations, product
from math import gcd,prod
from collections import Counter, defaultdict
from functools import cache
import json
A={1,2,10,11,12,16,17,22,25,26,30,31,32}
PER=2520
pts=tuple(v for v in range(PER) if v%35 in A)
FULL=(1<<len(pts))-1
F=(7,8,9,10,12,14,15,18,24,30,35)
FIX=((3,0),(3,1),(6,5))
caps={7:4,8:2,10:2,14:3,35:12,9:4,12:2,15:6,18:2,24:4,30:2}
def mask(f,b):
    return sum(1<<i for i,v in enumerate(pts) if v%f==b)
X=tuple(sorted(set(FIX)|{(f,b) for f in F for b in range(f) if mask(f,b)}))
M={x:mask(*x) for x in X}
def valid(xs):
    return all(n<=caps[f] for f,n in Counter(f for f,b in xs if (f,b) not in FIX).items())
def missing(xs):
    union=0
    for x in xs: union |= M[x]
    return FULL^union
def irredundant(xs):
    return all(missing(tuple(y for y in xs if y!=x)) for x in xs)
def local(r):
    return tuple(x for x in X if x[0]%3==0 and x[1]%3==r)
def phase_mask(r):
    return mask(3,r)
@cache
def solutions(holes, k, pool):
    # All inclusion-minimal subcovers of holes; only the given pool.
    if not holes: return ((),)
    if not k:return ()
    possible=tuple(x for x in pool if M[x]&holes)
    if not possible or sum(sorted(((M[x]&holes).bit_count() for x in possible),reverse=True)[:k]) < holes.bit_count(): return ()
    # choose a hole fewest possible channels cover
    ix=[i for i in range(len(pts)) if holes>>i&1]
    hit=min((tuple(x for x in possible if M[x]>>i&1) for i in ix), key=len)
    ans=set()
    for x in hit:
        for sub in solutions(holes&~M[x],k-1,tuple(y for y in possible if y!=x)):
            if all(M[y]&holes&~sum_union(M[z] for z in (*sub,x) if z!=y) for y in (*sub,x)):
                ans.add(tuple(sorted((*sub,x))))
    return tuple(sorted(ans))
def sum_union(e):
    u=0
    for x in e: u|=x
    return u
def classes():
    # Non-split branch: direct row geometry proved in v13.
    Z=(1,2,3,4,5)
    for omit in Z:
        rows=tuple((7,b) for b in Z if b!=omit)
        yield tuple(sorted((*rows,(14,omit),(14,omit+7))))
        remaining=sorted(v for v in A if v%7==omit)
        if len(remaining)==2: yield tuple(sorted((*rows,*((35,b) for b in remaining))))
    # Split branch: choose shared classes, then independently cover all 3 deficits.
    shares=tuple(x for x in X if x[0] in (8,10))
    for n in range(4):
        for common in combinations(shares,n):
            if not valid(common):continue
            left=missing(common)
            slices=tuple(solutions(left&phase_mask(r),4-n,local(r)) for r in range(3))
            for a,b,c in product(*slices):
                if min(map(len,(a,b,c)))<1 or n+sum(map(len,(a,b,c)))>6:continue
                s=tuple(sorted((*common,*a,*b,*c)))
                if valid(s) and irredundant(s): yield s
def main():
    templates=sorted(set(classes()))
    assert all(not missing(t) and valid(t) and irredundant(t) for t in templates)
    print('templates',len(templates),Counter((len(t),sum(x in ((3,0),(3,1)) for x in t)) for t in templates))
    print('signatures',len(set(tuple(x[0] for x in t) for t in templates)), 'supports',sorted(set(x[0] for t in templates for x in t)))
    B=set(FIX)
    witnesses={}
    for t in templates:
        xs=set(t)|B
        for x in t:
            if x not in B and x[0] not in witnesses and all(missing(tuple(y for y in xs if y!=x)) for _ in [0]):
                witnesses[x[0]]=(x,t)
    print('witnesses',witnesses)
    with open('templates.json','w') as f:
        json.dump({'period_v':PER,'types':templates,'essential_f':witnesses},f,separators=(',',':'))
if __name__=='__main__':main()
