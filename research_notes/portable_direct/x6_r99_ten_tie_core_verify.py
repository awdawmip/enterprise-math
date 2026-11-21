#!/usr/bin/env python3
"""R99 finite box and exact rational verification for a conditional positive-count BRC observer.
The infinite-domain theorem rests on the paper's integer congruence and exclusion proof,
not this finite q<=40 enumeration. No native X6 evolution or phase attribution is computed.
"""
from fractions import Fraction as Q
from math import lcm

P_MAX=40
CORE={
 (1,0,0):1, (4,-1,0):4, (5,-4,1):6, (6,-4,1):7,
 (9,-5,1):10, (10,-5,1):11, (14,-9,2):16,
 (15,-9,2):17, (19,-10,2):21, (24,-14,3):27,
}
EXCLUDED={
 (18,-10,2):20, (20,-13,3):23, (23,-14,3):26,
 (25,-14,3):28, (28,-15,3):31,
 (30,-18,4):34, (34,-19,4):38,
}
WITNESSES={
 (1,0,0):(Q(5),Q(13),11),
 (4,-1,0):(Q(1),Q(23),11),
 (5,-4,1):(Q(5),Q(11),11),
 (6,-4,1):(Q(1),Q(23),11),
 (9,-5,1):(Q(5),Q(11),11),
 (10,-5,1):(Q(1),Q(1),11),
 (14,-9,2):(Q(11),Q(1),16),
 (15,-9,2):(Q(5),Q(13),17),
 (19,-10,2):(Q(7),Q(11),21),
 (24,-14,3):(Q(11),Q(1),27),
}
WEIGHTS=[
 (Q(1),Q(1)),(Q(5),Q(11)),(Q(5),Q(13)),
 (Q(5),Q(23)),(Q(11),Q(1)),(Q(11),Q(11)),
 (Q(7),Q(11)),(Q(1),Q(23)),(Q(100),Q(100)),
 (Q(11),Q(12)),(Q(100),Q(12)),(Q(12),Q(100)),
 (Q(5,2),Q(11,2)),(Q(6),Q(12)),
 (Q(25),Q(100)),(Q(1000),Q(1000))
]

def canon(a):
    f=next(v for v in a if v)
    return a if f>0 else tuple(-v for v in a)

def port(a):
    return max(sum(max(v,0) for v in a),sum(max(-v,0) for v in a))

def gaps(a):
    x,y,z=a
    u=x+3*y+6*z
    v=3*x+12*y+30*z
    h=7*x+39*y+126*z
    return (abs(u),max(abs(v),abs(v-u)),
            max(abs(h),abs(h-u)),abs(h-v))

def scale(S,T):
    ns,ms=S.numerator,S.denominator
    nt,mt=T.numerator,T.denominator
    den3=ns*mt+nt*ms
    D=lcm(2,ns+ms,nt+mt,den3)
    return (D//2,ms*(D//(ns+ms)),
            mt*(D//(nt+mt)),ms*mt*(D//den3)),D

def score(g,m):
    return max(x*y for x,y in zip(g,m))

def envelope(S,T,p):
    e0=Q(1,2)
    ed=12/(T+1)
    eb=max(3/(S+1),6/(T+1))
    ec=6/(S+1)
    return min(e0,ed,eb,ec) if p>=27 else min(e0,ed,eb)

# Exact finite box implied by s,d,c and q<=26.
box=set()
for u in (-1,0,1):
 for k in range(-3,4):
  v=3*k
  for j in range(-3,4):
   h=u+6*j
   if abs(h)>12 or (j-k)%2:continue
   a=(10*u+3*j-12*k,-5*u-2*j+7*k,u+(j-3*k)//2)
   if a==(0,0,0):continue
   q=port(a)
   if q<=26 or abs(v)<=6:
    box.add(canon(a))
assert len(box)==17,len(box)
assert box==set(CORE)|set(EXCLUDED),box^set(CORE)^set(EXCLUDED)
assert all(port(a)==q for a,q in list(CORE.items())+list(EXCLUDED.items()))

DIRECTIONS=[]
for x in range(-P_MAX,P_MAX+1):
 for y in range(-P_MAX,P_MAX+1):
  for z in range(-P_MAX,P_MAX+1):
   if not(x or y or z):continue
   a=(x,y,z);q=port(a)
   if q<=P_MAX and canon(a)==a:
    DIRECTIONS.append((q,a,gaps(a)))
assert len(DIRECTIONS)==110740,len(DIRECTIONS)

checks=0
for S,T in WEIGHTS:
    m,D=scale(S,T)
    level=[None]*(P_MAX+1)
    tied=[set() for _ in range(P_MAX+1)]
    for q,a,g in DIRECTIONS:
        f=score(g,m)
        if level[q] is None or f<level[q]:
            level[q]=f;tied[q]={a}
        elif f==level[q]:
            tied[q].add(a)
    running=None;setnow=set()
    for p in range(1,P_MAX+1):
        if level[p] is not None:
            if running is None or level[p]<running:
                running=level[p];setnow=set(tied[p])
            elif level[p]==running:
                setnow.update(tied[p])
        if p>=11:
            expected=min(score(gaps(a),m)
                         for a,q in CORE.items() if q<=p)
            ties={a for a,q in CORE.items()
                  if q<=p and score(gaps(a),m)==expected}
            assert running==expected and setnow==ties,(S,T,p,setnow^ties)
            assert Q(expected,D)==envelope(S,T,p),(S,T,p)
            checks+=1

for a,(S,T,p) in WITNESSES.items():
    m,D=scale(S,T)
    val=score(gaps(a),m)
    expected=min(score(gaps(b),m) for b,q in CORE.items() if q<=p)
    assert val==expected and Q(val,D)==envelope(S,T,p),(a,S,T,p)

print({
 'status':'PASS',
 'full_unoriented_q_le_40':len(DIRECTIONS),
 'finite_box_directions':len(box),
 'minimal_universal_tie_core':len(CORE),
 'strictly_excluded_directions':len(EXCLUDED),
 'parameter_pairs':len(WEIGHTS),
 'port_budgets_per_pair':30,
 'exact_full_lattice_cases':checks,
 'essentiality_witnesses':len(WITNESSES),
 'arithmetic':'LCM-scaled exact integer, Fraction envelope',
 'universal_proof':'symbolic bounded box + strict exclusions'
})
