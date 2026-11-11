#!/usr/bin/env python3
"""R86: exact persistent winner-profile AVL for auxiliary rational circle sources.
Arbitrary versioned (time, branch) identities; fixed rational query signature.
Uses only exact Fraction arithmetic. The cache is per-time, never per-version.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from bisect import bisect_left
from math import floor, ceil
from random import Random
import json

L, U = F(1, 6), F(2, 5)
J, X, A, B = 2, F(1, 7), 1, 3
cache = {}
counts = dict(time_profiles=0, allocated_nodes=0, merged_atoms=0, version_checks=0, direct_atoms=0)

def frac(x): return x - floor(x)

def member(t, theta):
    a, b, s = frac(A*theta), frac(B*theta), frac(X+(t-J)*theta)
    return (a <= s < b) if a < b else ((s >= a or s < b) if a > b else False)

def linear_cuts(slope, offset=F(0)):
    if not slope: return set()
    lo, hi = sorted((offset+slope*L, offset+slope*U))
    return {(F(k)-offset)/slope for k in range(ceil(lo), floor(hi)+1)}

def critical(t):
    c = {L,U}
    for slope,off in ((A,F(0)),(B,F(0)),(A-B,F(0)),
                      (t-J,X),(t-J-A,X),(t-J-B,X)):
        c.update(linear_cuts(slope,off))
    return tuple(sorted(z for z in c if L<=z<=U))

@dataclass(frozen=True)
class Profile:
    points: tuple
    at: tuple
    gap: tuple

def value(profile,z):
    i = bisect_left(profile.points,z)
    if i < len(profile.points) and profile.points[i]==z: return profile.at[i]
    assert 0 < i < len(profile.points)
    return profile.gap[i-1]

def tagged(t, branch):
    if t not in cache:
        c=critical(t)
        cache[t]=(c,tuple(member(t,z) for z in c),
                  tuple(member(t,(l+r)/2) for l,r in zip(c,c[1:])))
        counts['time_profiles']+=1
    p,at,gap=cache[t]
    tag=(t,branch)
    return Profile(p,tuple(tag if yes else None for yes in at),
                   tuple(tag if yes else None for yes in gap))

def maximum(*values):
    return max((x for x in values if x is not None),default=None)

def overlay(profiles):
    profiles=[p for p in profiles if p is not None]
    assert profiles
    if len(profiles)==1:return profiles[0]
    points=tuple(sorted(set().union(*(p.points for p in profiles))))
    at=tuple(maximum(*(value(p,z) for p in profiles)) for z in points)
    gaps=tuple(maximum(*(value(p,(l+r)/2) for p in profiles))
               for l,r in zip(points,points[1:]))
    counts['merged_atoms']+=len(at)+len(gaps)
    return Profile(points,at,gaps)

@dataclass(frozen=True)
class Node:
    t:int
    branches:tuple
    left:object
    right:object
    h:int
    winner:Profile

def height(n):return n.h if n else 0

def make(t,branches,left=None,right=None):
    assert branches and tuple(sorted(set(branches)))==branches
    p=tagged(t,branches[-1])
    n=Node(t,branches,left,right,1+max(height(left),height(right)),
           overlay([p,left.winner if left else None,right.winner if right else None]))
    counts['allocated_nodes']+=1
    return n

def rot_l(n):
    r=n.right
    return make(r.t,r.branches,make(n.t,n.branches,n.left,r.left),r.right)

def rot_r(n):
    l=n.left
    return make(l.t,l.branches,l.left,make(n.t,n.branches,l.right,n.right))

def balance(n):
    delta=height(n.left)-height(n.right)
    if delta>1:
        if height(n.left.right)>height(n.left.left):
            n=make(n.t,n.branches,rot_l(n.left),n.right)
        return rot_r(n)
    if delta< -1:
        if height(n.right.left)>height(n.right.right):
            n=make(n.t,n.branches,n.left,rot_r(n.right))
        return rot_l(n)
    return n

def pop_min(n):
    if n.left is None:return n,n.right
    item,other=pop_min(n.left)
    return item,balance(make(n.t,n.branches,other,n.right))

def put(n,t,b,add):
    if not n:return make(t,(b,)) if add else None
    if t<n.t:return balance(make(n.t,n.branches,put(n.left,t,b,add),n.right))
    if t>n.t:return balance(make(n.t,n.branches,n.left,put(n.right,t,b,add)))
    br=set(n.branches)
    if add:br.add(b)
    else:br.discard(b)
    if br:return make(t,tuple(sorted(br)),n.left,n.right)
    if not n.left:return n.right
    if not n.right:return n.left
    suc,right=pop_min(n.right)
    return balance(make(suc.t,suc.branches,n.left,right))

def audit_tree(n):
    if not n:return set(),0
    ls,lh=audit_tree(n.left)
    rs,rh=audit_tree(n.right)
    assert (not ls or max(t for t,b in ls)<n.t)
    assert (not rs or min(t for t,b in rs)>n.t)
    assert abs(lh-rh)<=1 and n.h==max(lh,rh)+1
    s=ls|rs|{(n.t,b) for b in n.branches}
    return s,n.h

def direct(events,z):
    return maximum(*((t,b) for t,b in events if member(t,z)))

def check(n,events):
    s,h=audit_tree(n)
    assert s==events
    if not n: assert not events;return
    times={t for t,b in events}
    pts=tuple(sorted(set().union(*(critical(t) for t in times))))
    probes=pts+tuple((l+r)/2 for l,r in zip(pts,pts[1:]))
    for z in probes:
        assert value(n.winner,z)==direct(events,z),(z,value(n.winner,z),direct(events,z))
    assert n.winner.points[0]==L and n.winner.points[-1]==U
    counts['version_checks']+=1
    counts['direct_atoms']+=len(probes)

def version_decision(n):
    if n is None:return ('STABLE_NONE',None)
    p=n.winner
    zs=p.points+tuple((a+b)/2 for a,b in zip(p.points,p.points[1:]))
    vals=p.at+p.gap
    if all(v==vals[0] for v in vals):
        return ('STABLE_NONE',None) if vals[0] is None else ('STABLE',vals[0])
    for z,v in zip(zs,vals):
        if v!=vals[0]:return ('CHANGES',(p.points[0],vals[0]),(z,v))
    raise AssertionError('unreachable')

def run():
    global L, U, J, X, A, B
    rng=Random(8620261112)
    root=None;events=set();history=[]
    for k in range(72):
        t,b=rng.randrange(-8,9),rng.randrange(4)
        if (t,b) in events:
            events.remove((t,b));root=put(root,t,b,False)
        else:
            events.add((t,b));root=put(root,t,b,True)
        check(root,events)
        d=version_decision(root)
        if d[0]=='CHANGES':
            assert direct(events,d[1][0])==d[1][1]
            assert direct(events,d[2][0])==d[2][1]
            assert d[1][1]!=d[2][1]
        history.append((root,frozenset(events)))
        if k%9==0:
            old,old_events=history[rng.randrange(len(history))]
            check(old,set(old_events))
    for old,old_events in history[::10]:check(old,set(old_events))
    # Branch-only updates preserve the time predicate but can change the branch winner.
    a=put(None,6,1,True);b=put(a,6,2,True)
    assert any(v==(6,1) for v in a.winner.at+a.winner.gap)
    assert any(v==(6,2) for v in b.winner.at+b.winner.gap)
    assert value(a.winner,F(3,10))==(6,1) or not member(6,F(3,10))
    # Original label coincidences are explicit point atoms.
    for z in (F(0),F(1,2)):
        assert not member(5,z) if frac(A*z)==frac(B*z) else True
    # Cross-signature exact tests, including negative coefficients and degenerate arcs.
    main_query=(L,U,J,X,A,B)
    suite_count=24
    for suite in range(suite_count):
        L,U=F(-1,4),F(3,5)
        J=rng.randrange(-4,5)
        X=F(rng.randrange(-10,11),rng.randrange(1,8))
        A=rng.randrange(-5,6);B=rng.randrange(-5,6)
        cache.clear()
        root2=None;E2=set()
        for step in range(14):
            t,b=rng.randrange(-7,8),rng.randrange(4)
            if (t,b) in E2:E2.remove((t,b));root2=put(root2,t,b,False)
            else:E2.add((t,b));root2=put(root2,t,b,True)
            check(root2,E2)
            v=version_decision(root2)
            if v[0]=='CHANGES':
                assert direct(E2,v[1][0])==v[1][1]
                assert direct(E2,v[2][0])==v[2][1]
                assert v[1][1]!=v[2][1]
    L,U,J,X,A,B=main_query
    out={'schema':'EM_R86_EXACT_PERSISTENT_WINNER_PROFILE_V1','cross_signature_suites':suite_count,
         'model':'auxiliary rational circle source, finite rational interval, original directed half-open arc',
         'frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
         'query':{'L':str(L),'U':str(U),'j':J,'x':str(X),'a':A,'b':B},
         'random_seed':8620261112,'updates':72,
         'historical_versions':len(history),
         **counts,'distinct_time_cache_entries':len(cache),
         'status':'ALL_ASSERTIONS_PASS',
         'limitations':['fixed query signature, bounded time trials; author-side exact arithmetic',
                        'no runtime/crossover benchmark','winner-profile merge size not logarithmically bounded',
                        'no native BRC dynamics or formal independent review']}
    print('R86_PASS',out['version_checks'],out['direct_atoms'],out['time_profiles'],out['allocated_nodes'])
    with open('verification.json','w') as f:json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
if __name__=='__main__':run()
