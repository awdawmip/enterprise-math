#!/usr/bin/env python3
"""Exact Port-10 six-pair BRC halfstrip certificate; no external dependencies."""
from fractions import Fraction as Q
from itertools import combinations

PAIR = tuple(combinations(range(4), 2))
KEEP = {(1,0,0),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(9,-5,1)}
REGIONS = {
    'P0': (6, 'BD', ((0,500),(20,500),(20,568),(0,528)), False),
    'P1': (2, 'BC', ((0,528),(20,568),(20,1156),(0,1056)), False),
    'P2': (12,'BD', ((0,1056),(20,1156)), True),
}

def port(a):
    return max(sum(max(v,0) for v in a),sum(max(-v,0) for v in a))

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[j]-h[i]) for i,j in PAIR)

def population():
    return {a:gaps(a) for x in range(-10,11)
            for y in range(-10,11)
            for z in range(-10,11)
            if (a:=(x,y,z))!=(0,0,0)
            and a > tuple(-v for v in a) and port(a)<=10}

def capacities(b,d):
    w=(136,b,176,d)
    return tuple(w[i]+w[j] for i,j in PAIR)

def L(which,b,d):
    return b+d if which=='BD' else b+176

def witness(g, spec, factor, rhs):
    K,which,vertices,ray=spec
    for j in range(6):
        if all(factor*g[j]*L(which,b,d)>=rhs*K*capacities(b,d)[j]
               for b,d in vertices):
            if not ray or factor*g[j]*(1 if which=='BD' else 0)>=rhs*K*(j in (2,4,5)):
                return j
    return None

def upper(a,spec):
    K,which,vertices,ray=spec
    g=gaps(a)
    assert all(g[j]*L(which,b,d)<=K*capacities(b,d)[j]
               for b,d in vertices for j in range(6))
    assert not ray or all(g[j]*(1 if which=='BD' else 0)<=K*(j in (2,4,5)) for j in range(6))
    # One pair equality on the entire region (linear form vanishes at vertices).
    assert any(all(g[j]*L(which,b,d)==K*capacities(b,d)[j] for b,d in vertices)
               and (not ray or g[j]*(1 if which=='BD' else 0)==K*(j in (2,4,5))) for j in range(6))

def predicted(b,d):
    t1=528+2*b; t2=704+3*b; t3=1224+8*b; t4=1584+8*b; t5=2448+17*b
    near={(1,0,0),(5,-4,1),(5,-1,0)}
    if d<t1: near.add((9,-5,1))
    if d>t2: near|={(4,-1,0),(6,-4,1)}
    if d>=t3: near.remove((5,-1,0))
    if d>=t4: near-={(1,0,0),(5,-4,1)}
    if d>=t5: near.remove((4,-1,0))
    eta=(Q(6,b+d) if d<=t1 else Q(2,b+176) if d<=1056+5*b else Q(12,b+d))
    return eta,near

def brute(gaps_by_a,b,d):
    den=capacities(b,d)
    scores={a:max(Q(g[j],den[j]) for j in range(6)) for a,g in gaps_by_a.items()}
    eta=min(scores.values())
    return eta,{a for a,v in scores.items() if 2*v<3*eta}

def main():
    pop=population()
    assert len(pop)==1935 and KEEP <=pop.keys()
    for name,spec in REGIONS.items():
        assert all(witness(g,spec,1,1) is not None for g in pop.values()), name
        assert all(witness(g,spec,2,3) is not None for a,g in pop.items() if a not in KEEP),name
        upper((6,-4,1) if name=='P2' else (1,0,0),spec)
    count=0
    for b in (Q(1,2),Q(8),Q(20)):
        walls=(528+2*b,704+3*b,1224+8*b,1584+8*b,2448+17*b)
        tests={Q(500),Q(10000),Q(3000)}
        for t in walls:tests|={t-Q(1,2),t,t+Q(1,2)}
        for d in sorted(tests):
            if d<500:continue
            assert predicted(b,d)==brute(pop,b,d),(b,d)
            count+=1
    print('R137 HALFROM STRIP CERTIFICATE PASS')
    print('unoriented_population',len(pop),'uniformly_excluded_outsiders',len(pop)-len(KEEP))
    print('optimizer_lower_checks',len(pop)*len(REGIONS))
    print('outsider_exclusions', (len(pop)-len(KEEP))*len(REGIONS))
    print('rational_full_population_replays',count)
    print('optimizer_switches','D=528+2B','D=1056+5B')
    print('near_change_walls','528+2B','704+3B','1224+8B','1584+8B','2448+17B')

if __name__=='__main__':main()
