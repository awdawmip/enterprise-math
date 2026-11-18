#!/usr/bin/env python3
"""Exact dyadic-gap overlap against the E+256 symmetric-panel collision union.

Uses frozen p=32 named-XOR observer and the exact PREFIX-895 special set U.
All 2,097,153 increasing positive-gap modulus pairs are examined.
"""
import math, json
N=1<<32
T=33*N
Q=range(262145,524288,2)
S={262147,280001,300001,320003,340007,360007,380003,400009,
   420001,440003,460001,480007,500383,510007,520001,524285}
U=S|set(range(400011,400522,2))|set(range(480011,480522,2))
U|={q for q in Q if any(((1<<h)-1)%q==0 or ((1<<h)+1)%q==0 for h in range(1,32))}
assert len(U)==552
P3={c+194*j for c in (510001,510003,510005) for j in range(64)}
B={510009+194*j for j in range(64)}
P4=P3|B
assert len(P3)==192 and len(P4)==256 and not P4&U

def E(a,b):
    return (a*b<T or a in U or b in U or
            a//math.gcd(a,b)*b<N or
            33*((N+a-1)//a)>b or 33*((N+b-1)//b)>a)

rows=[]
for h in range(1,18):
    gap=1<<h
    d={'h':h,'gap':gap,'all':0,'E':0,'P3':0,'P4':0,
       'E_and_P3':0,'E_and_P4':0,'new_P3':0,
       'new_P4':0,'lost_to_B':0}
    for a in range(262145,524288-gap,2):
        b=a+gap
        e=E(a,b)
        p3=a in P3 or b in P3
        p4=a in P4 or b in P4
        d['all']+=2
        d['E']+=2*e
        d['P3']+=2*p3
        d['P4']+=2*p4
        d['E_and_P3']+=2*(e and p3)
        d['E_and_P4']+=2*(e and p4)
        d['new_P3']+=2*(not e and not p3)
        d['new_P4']+=2*(not e and not p4)
        d['lost_to_B']+=2*(not e and not p3 and p4)
    assert d['new_P3']-d['new_P4']==d['lost_to_B']
    rows.append(d)
tot={k:sum(r[k] for r in rows) for k in rows[0] if k not in ('h','gap')}
assert tot['new_P3']==2336712
assert tot['new_P4']==2333220 and tot['lost_to_B']==3492
assert tot['E']==1846732 and tot['P4']==14376 and tot['E_and_P4']==22
panel_256=7630612196
dyadic_192=7617211750
combined=panel_256+tot['new_P4']
assert combined==7632945416
assert combined-dyadic_192==15733666
assert len(Q)**2-combined==9546923768
print(json.dumps({'per_gap':rows,'totals':tot,
  'panel_256':panel_256,'dyadic_192':dyadic_192,
  'combined':combined,'net_vs_PREFIX903':combined-dyadic_192,
  'uncovered':len(Q)**2-combined},indent=2,sort_keys=True))
