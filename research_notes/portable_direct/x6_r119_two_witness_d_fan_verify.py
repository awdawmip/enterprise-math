#!/usr/bin/env python3
"""X6 R119 exact rational replay of the two-witness D fan.

The paper supplies the infinite-lattice proof; this program independently
enumerates every unoriented integer vector with Port <= 38.
"""
from fractions import Fraction
import json

P = 38
ROWS = [(0,1,-1),(0,1,1),(0,2,0),(1,-2,0),(1,0,0),(1,2,0),
        (1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]
PORTS = (11,16,17,21,27,28,38)
DS = [Fraction(1),Fraction(10),Fraction(47),Fraction(47001,1000),
      Fraction(60),Fraction(70),Fraction(71),Fraction(75),
      Fraction(542,7),Fraction(78),Fraction(181,2),Fraction(91),
      Fraction(211,2),Fraction(106),Fraction(107),Fraction(110),Fraction(121)]

def inverse(t,m,n):
    assert (m-n)%2 == 0
    return (10*t-12*m+3*n,-5*t+7*m-2*n,t+(n-3*m)//2)

def canonical(v):
    return min(v,tuple(-x for x in v))

def port(v):
    return max(sum(max(x,0) for x in v),sum(max(-x,0) for x in v))

def gaps(v):
    x,y,z=v
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return (abs(h[0]-h[1]),abs(h[0]-h[2]),abs(h[0]-h[3]),
            abs(h[1]-h[2]),abs(h[1]-h[3]),abs(h[2]-h[3]))

bank={canonical(inverse(*row)) for row in ROWS}
assert len(bank)==10
vectors=[]
for x in range(-P,P+1):
    for y in range(-P,P+1):
        for z in range(-P,P+1):
            v=(x,y,z)
            if v==(0,0,0) or canonical(v)!=v:
                continue
            q=port(v)
            if q<=P:
                vectors.append((v,q,gaps(v)))
assert len(vectors)==95133,len(vectors)

records=[]
for D in DS:
    d=D.denominator
    n=D.numerator
    eta=Fraction(1,12) if D<=71 else 6/(D+1)
    en,ed=eta.numerator,eta.denominator
    # Denominators of AB, AC, AD, BC, BD, CD, all multiplied by d.
    sums=(12*d,71*d,11*d+n,61*d,d+n,60*d+n)
    def below_eta(gaps):
        return all(g*ed*d < en*w for g,w in zip(gaps,sums))
    def near(gaps):
        return all(2*g*ed*d < 3*en*w for g,w in zip(gaps,sums))
    got=set()
    by_port={p:set() for p in PORTS}
    for v,q,gs in vectors:
        assert not below_eta(gs),(str(D),v,"below eta")
        if near(gs):
            got.add(v)
            for p in PORTS:
                if q<=p:
                    by_port[p].add(v)
    expected={v for v in bank if near(gaps(v))}
    assert got==expected,(str(D),sorted(got^expected))
    if D<=47: count=4
    elif D<Fraction(542,7): count=10
    elif D<Fraction(181,2): count=9
    elif D<Fraction(211,2): count=8
    elif D<107: count=7
    else: count=2
    assert len(got)==count,(str(D),len(got),count)
    records.append({"D":str(D),"eta":str(eta),"near_at_port38":len(got),
                    "port_counts":{str(p):len(by_port[p]) for p in PORTS},
                    "below_eta":0,"outside_ten_row_bank":0})

result={"schema":"X6_R119_TWO_WITNESS_D_FAN_EXACT_REPLAY_V1",
        "scientific_model":"conditional all-six-pair BRC observer",
        "finite_replay_port_cap":P,"samples":len(DS),
        "unoriented_vectors_per_sample":len(vectors),
        "vector_sample_pairs":len(vectors)*len(DS),
        "cases":records,"author_replay":"PASS",
        "independent_review":"NOT_PERFORMED"}
print(json.dumps(result,indent=2))
