"""R88: persistent time/fiber AVL + exact two-polarity champion oracle.
Auxiliary rational circular-source model; standard library only.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from collections import Counter
from random import Random
from time import perf_counter_ns
import json

@dataclass(frozen=True)
class Node:
    time: int
    branches: frozenset[int]
    left: Node|None
    right: Node|None
    height: int
    times: int
    identities: int

def h(n): return n.height if n else 0
def nt(n): return n.times if n else 0
def ni(n): return n.identities if n else 0

ALLOC = Counter()
def make(t, bs, l=None, r=None):
    assert bs
    ALLOC['nodes'] += 1
    return Node(t,bs,l,r,1+max(h(l),h(r)),1+nt(l)+nt(r),len(bs)+ni(l)+ni(r))
def rot_l(n):
    r=n.right
    return make(r.time,r.branches,make(n.time,n.branches,n.left,r.left),r.right)
def rot_r(n):
    l=n.left
    return make(l.time,l.branches,l.left,make(n.time,n.branches,l.right,n.right))
def balance(n):
    d=h(n.left)-h(n.right)
    if d>1:
        l=n.left
        if h(l.left)<h(l.right): n=make(n.time,n.branches,rot_l(l),n.right)
        return rot_r(n)
    if d< -1:
        r=n.right
        if h(r.right)<h(r.left): n=make(n.time,n.branches,n.left,rot_r(r))
        return rot_l(n)
    return n

def pop_min(n):
    if n.left is None: return n,n.right
    first,newleft=pop_min(n.left)
    return first,balance(make(n.time,n.branches,newleft,n.right))

def toggle(n,t,b):
    if n is None: return make(t,frozenset([b]))
    if t<n.time:return balance(make(n.time,n.branches,toggle(n.left,t,b),n.right))
    if t>n.time:return balance(make(n.time,n.branches,n.left,toggle(n.right,t,b)))
    bs=n.branches ^ {b}
    if bs:return make(t,frozenset(bs),n.left,n.right)
    if n.left is None:return n.right
    if n.right is None:return n.left
    successor,newright=pop_min(n.right)
    return balance(make(successor.time,successor.branches,n.left,newright))

def descending(n):
    if n is not None:
        yield from descending(n.right)
        yield (n.time,max(n.branches))
        yield from descending(n.left)

def collect(n):
    if n is None:return frozenset()
    return collect(n.left)|frozenset((n.time,b) for b in n.branches)|collect(n.right)

def validate(n,lo=None,hi=None):
    if n is None:return 0,0,0
    assert (lo is None or lo<n.time) and (hi is None or n.time<hi)
    lh,lc,li=validate(n.left,lo,n.time)
    rh,rc,ri=validate(n.right,n.time,hi)
    assert abs(lh-rh)<=1 and n.height==1+max(lh,rh)
    assert n.times==1+lc+rc and n.identities==len(n.branches)+li+ri
    return n.height,n.times,n.identities

def frac(z):return z-z.numerator//z.denominator

def member(t,theta,j,x,a,b):
    s,A,B=frac(x+(t-j)*theta),frac(a*theta),frac(b*theta)
    return ((A<=s<B) if A<B else (s>=A or s<B) if A>B else False)

def cuts(t,I,j,x,a,b):
    L,U=I; out={L,U}
    for c,d in [(a,Q(0)),(b,Q(0)),(a-b,Q(0)),(t-j,x),(t-j-a,x),(t-j-b,x)]:
        if c==0:continue
        f,g=sorted((c*L+d,c*U+d))
        low=-((-f.numerator)//f.denominator)
        high=g.numerator//g.denominator
        for k in range(low,high+1):
            p=(Q(k)-d)/c
            if L<=p<=U:out.add(p)
    return sorted(out)

def atoms(points):
    for i,p in enumerate(points):
        yield p
        if i+1<len(points):yield (p+points[i+1])/2

def exact_polarity(t,want,I,j,x,a,b,stats):
    stats['oracles']+=1
    for p in atoms(cuts(t,I,j,x,a,b)):
        stats['oracle_atoms']+=1
        if member(t,p,j,x,a,b)==want:return p
    return None

def point_winner(root,theta,j,x,a,b,stats):
    for t,br in descending(root):
        stats['point_tests']+=1
        if member(t,theta,j,x,a,b):return (t,br)
    return None

def certified_winner(root,I,j,x,a,b,cache,stats):
    """Global STABLE/CHANGES result; all parameters are rationals, I closed."""
    L,_=I;w0=point_winner(root,L,j,x,a,b,stats)
    def exists(t,want):
        key=(I,j,x,a,b,t,want)
        if key in cache:
            stats['hits']+=1
        else:cache[key]=exact_polarity(t,want,I,j,x,a,b,stats)
        return cache[key]
    if w0 is None:
        for t,_ in descending(root):
            q=exists(t,True)
            if q is not None:
                w=point_winner(root,q,j,x,a,b,stats)
                assert w is not None
                return ('CHANGES',(L,None),(q,w))
        return ('STABLE_NONE',None,None)
    for t,_ in descending(root):
        if t<=w0[0]:break
        q=exists(t,True)
        if q is not None:
            w=point_winner(root,q,j,x,a,b,stats)
            assert w>w0
            return ('CHANGES',(L,w0),(q,w))
    q=exists(w0[0],False)
    if q is not None:
        w=point_winner(root,q,j,x,a,b,stats)
        assert w!=w0
        return ('CHANGES',(L,w0),(q,w))
    return ('STABLE',w0,None)

def independent_full_profile(present,I,j,x,a,b,stats):
    pt={*I}
    for t in set(t for t,_ in present):
        stats['reference_profiles']+=1
        pt.update(cuts(t,I,j,x,a,b))
    out=[]
    for theta in atoms(sorted(pt)):
        stats['reference_atoms']+=1
        w=next(((t,br) for t,br in sorted(present,reverse=True) if member(t,theta,j,x,a,b)),None)
        out.append((theta,w))
    if all(w==out[0][1] for _,w in out):
        return ('STABLE_NONE' if out[0][1] is None else 'STABLE',out[0][1])
    return ('CHANGES',None)

def run():
    rng=Random(8820261112)
    data=Counter(); signatures=set(); cache={}; roots=[]
    # Source updates, historical queries, tied time fibers and exact full-real reference.
    for trial in range(48):
        L=Q(rng.randint(-3,2),rng.randint(3,10)); U=L+Q(rng.randint(0,3),rng.randint(5,16))
        I=(L,U);j=rng.randint(-4,4);x=Q(rng.randint(-4,4),rng.randint(2,8));a=rng.randint(-5,5);b=rng.randint(-5,5)
        root=None; present=set(); history=[]
        for k in range(10):
            who=(rng.randint(-18,18),rng.randint(-2,2))
            present.symmetric_difference_update({who})
            old_root=root
            root=toggle(root,*who)
            history.append((root,frozenset(present)))
            validate(root)
            assert collect(root)==frozenset(present)
            if old_root is not None:validate(old_root)
            data['edits']+=1
            for root2,refset in [history[-1],history[rng.randrange(len(history))]]:
                ans=certified_winner(root2,I,j,x,a,b,cache,data)
                ref=independent_full_profile(refset,I,j,x,a,b,data)
                assert ans[0]==ref[0],(trial,k,ans,ref,I,j,x,a,b,refset)
                if ans[0]=='STABLE':assert ans[1]==ref[1]
                if ans[0]=='CHANGES':
                    for p,w in ans[1:]:
                        assert I[0]<=p<=I[1]
                        assert w==next(((t,z) for t,z in sorted(refset,reverse=True) if member(t,p,j,x,a,b)),None)
                    assert ans[1][1]!=ans[2][1]
                    data['changes']+=1
                data['version_comparisons']+=1
        roots.append(history)
    # Same time with multiple branches: membership cache is safe; a time-only result quotient is not.
    I=(Q(1,4),Q(1,4));j=0;x=Q(0);a=1;b=2
    r=None
    for who in [(1,1),(1,7)]:r=toggle(r,*who)
    assert certified_winner(r,I,j,x,a,b,{},Counter())[1]==(1,7)
    old=r;r=toggle(r,1,7)
    assert certified_winner(r,I,j,x,a,b,{},Counter())[1]==(1,1)
    assert certified_winner(old,I,j,x,a,b,{},Counter())[1]==(1,7)
    data['branch_fiber_counterexamples']+=1
    # A high stable champion: exact certificate visits one time regardless of lower identities.
    family=[]
    for n in (32,128,512):
        root=None
        for t in range(1,n+1):root=toggle(root,t,0)
        top=(4*n+1,1);root=toggle(root,*top)
        interval=(Q(1,4),Q(1,4)+Q(1,10**8))
        sc=Counter();before=perf_counter_ns();res=certified_winner(root,interval,0,Q(0),1,2,{},sc)
        quick_ns=perf_counter_ns()-before
        assert res[:2]==('STABLE',top)
        ref_stats=Counter(); start=perf_counter_ns()
        ref=independent_full_profile(collect(root),interval,0,Q(0),1,2,ref_stats)
        reference_ns=perf_counter_ns()-start
        assert ref==('STABLE',top)
        family.append(dict(identities=n+1,certifier_oracles=sc['oracles'],point_tests=sc['point_tests'],
                           certifier_ns=quick_ns,reference_ns=reference_ns,
                           reference_source_profiles=ref_stats['reference_profiles'],reference_atoms=ref_stats['reference_atoms'],
                           persistent_height=root.height))
    return dict(seed=8820261112,random_edits=data['edits'],historical_version_comparisons=data['version_comparisons'],
                exact_changes=data['changes'],oracle_calls=data['oracles'],oracle_cache_hits=data['hits'],
                oracle_atom_tests=data['oracle_atoms'],reference_atom_tests=data['reference_atoms'],
                reference_profiles=data['reference_profiles'],nodes_allocated=ALLOC['nodes'],
                branch_fiber_counterexamples=data['branch_fiber_counterexamples'],top_stable_family=family,
                checks='PASS',timer='Python perf_counter_ns; single-run indicative, not benchmark confidence intervals')

if __name__=='__main__':
    r=run()
    with open(__file__.replace('check_r88.py','verification.json'),'w',encoding='utf-8') as fh:
        json.dump(r,fh,ensure_ascii=False,indent=2);fh.write('\n')
    print('R88_PASS',r['random_edits'],r['historical_version_comparisons'],r['oracle_calls'],r['oracle_cache_hits'],r['nodes_allocated'])
