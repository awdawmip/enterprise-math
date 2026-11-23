"""R152 exact Port-10 BRC six-pair bridge/tail atlas crosscheck.
Frozen scientific input R121@8085ff66, R122@0687aa24.
Recomputes all 1,935 unoriented integer directions for rational probes.
This is a static three-axis conditional BRC observer, not native time evolution.
"""
from fractions import Fraction as Q
from collections import Counter

A=(1,0,0); J=(4,-1,0); C=(5,-4,1)
K=(5,-1,0); E=(6,-4,1); H=(9,-5,1)
W=(A,J,C,K,E,H)

def directions():
    for x in range(-10,11):
        for y in range(-10,11):
            for z in range(-10,11):
                v=(x,y,z)
                if not any(v) or next(t for t in v if t)<0:
                    continue
                if max(sum(max(t,0) for t in v),sum(max(-t,0) for t in v)) <= 10:
                    yield v

def gaps(v):
    x,y,z=v
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[j]-h[i]) for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))

def score(g,B,D):
    capacities=(136+B,Q(312),136+D,B+176,B+D,176+D)
    return max(Q(gap)/cap for gap,cap in zip(g,capacities))

def pred(B,D):
    assert Q(20)<B<Q(136) and D>=Q(528)
    t_e=min(704+3*B,832-B)
    t_h=528+2*B if B<=32 else 1056+5*B
    u=1872-B
    t=2448+17*B
    out=set()
    if D<min(1584+8*B,u): out.update((A,C))
    if D<min(1224+8*B,u): out.add(K)
    if D<t_h: out.add(H)
    if t_e<D<t: out.add(J)
    if D>t_e: out.add(E)
    return out

def main():
    pop=list(directions())
    assert len(pop)==1935
    gp={v:gaps(v) for v in pop}
    cases=set()
    Bs=[Q(2001,100),Q(21),Q(3199,100),Q(32),Q(3201,100),
        Q(50),Q(7199,100),Q(72),Q(7201,100),Q(100),Q(13599,100)]
    for B in Bs:
        bounds=[Q(528),704+3*B,832-B,528+2*B,1056+5*B,
             1224+8*B,1584+8*B,1872-B,2448+17*B]
        for d in bounds:
            for eps in (Q(-1,100),Q(0),Q(1,100)):
                if d+eps>=528: cases.add((B,d+eps))
        for d in [Q(600),Q(1000),Q(1400),Q(1700),Q(1900),Q(3000),Q(5000)]:
            cases.add((B,d))
    for i in range(50):
        B=Q(20001+229*i,1000)
        D=Q(528)+Q((357*i)%4500)+Q(1,7)
        cases.add((B,D))
    count=Counter(); atL={}
    for B,D in sorted(cases):
        vals={v:score(gp[v],B,D) for v in pop}
        eta=min(vals.values())
        actual={v for v,f in vals.items() if 2*f<3*eta}
        expected=pred(B,D)
        assert actual==expected,(B,D,eta,sorted(actual),sorted(expected))
        assert eta==min(vals[v] for v in W)
        if D==1872-B: atL[str(B)]=len(actual)
        count[len(actual)]+=1
    print('R152 FULL MIDDLE BRIDGE-TO-TAIL ATLAS PASS')
    print('complete_integer_directions',len(pop),'exact_rational_full_population_cases',len(cases))
    print('count_histogram',dict(sorted(count.items())))
    print('L(B)=1872-B counts',atL)
    print('sharp cuts B=32 and B=72; all equality probes tested')
if __name__=='__main__': main()
