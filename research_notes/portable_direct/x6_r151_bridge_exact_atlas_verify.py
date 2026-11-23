"""R151 exact rational check of Port-10 six-pair static BRC bridge atlas.
Only conditional three-axis observer; not native dynamics/residual inference.
Frozen: R121@8085ff66 / R122@0687aa24. Python >=3.10 standard library.
"""
from fractions import Fraction as Q
from collections import Counter

W = {
 (1,0,0):(1,3,7,2,6,4),
 (4,-1,0):(1,0,11,1,12,11),
 (5,-4,1):(1,3,5,2,6,8),
 (5,-1,0):(2,3,4,1,6,7),
 (6,-4,1):(0,0,12,0,12,12),
 (9,-5,1):(0,3,6,3,6,3),
}
a,b,c,d,e,f=tuple(W)

def directions():
 for x in range(-10,11):
  for y in range(-10,11):
   for z in range(-10,11):
    v=(x,y,z)
    if not any(v) or next(k for k in v if k)<0: continue
    if max(sum(max(k,0) for k in v),sum(max(-k,0) for k in v))<=10:
     yield v

def gaps(v):
 x,y,z=v
 h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
 return tuple(abs(h[j]-h[i]) for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))

def score(g,B,D):
 s=(136+B,312,136+D,B+176,B+D,176+D)
 return max(Q(n,t) for n,t in zip(g,s))

def predicted(B,D):
 assert 20<B<136 and 528<=D<1872-B
 S=set()
 if D<1584+8*B: S|={a,c}
 if D<1224+8*B: S.add(d)
 if D<(528+2*B if B<=32 else 1056+5*B): S.add(f)
 if D>min(704+3*B,832-B): S|={b,e}
 return S

def main():
 pop=list(directions())
 assert len(pop)==1935 and len(set(pop))==1935
 g={v:gaps(v) for v in pop}
 assert {v:g[v] for v in W}==W
 cases=set()
 # Boundaries and their exact strict-equality neighbors across B=32 and B=72.
 Bs=[Q(201,10),Q(21),Q(30),Q(3199,100),Q(32),Q(3201,100),
     Q(40),Q(60),Q(7199,100),Q(72),Q(7201,100),Q(100),Q(135),Q(13599,100)]
 for B in Bs:
  ts=[Q(528),Q(656),Q(1872)-B,
      Q(704)+3*B,Q(832)-B,Q(1224)+8*B,Q(1584)+8*B,
      Q(528)+2*B,Q(1056)+5*B,Q(1248)-B]
  for t in ts:
   for delta in (Q(-1,100),Q(0),Q(1,100)):
    D=t+delta
    if Q(528)<=D<Q(1872)-B: cases.add((B,D))
  for D in (Q(528),Q(600),Q(800),Q(1100),Q(1400),Q(1700)):
   if Q(528)<=D<Q(1872)-B: cases.add((B,D))
 # Rational off-boundary cases, deterministic; no stochastic failure ambiguity.
 for j in range(70):
  B=Q(2001+j*17,100) # only retain points within strip
  if not 20<B<136: continue
  D=Q(528)+Q((j*157)%1100,1)+Q(1,7)
  if D<1872-B: cases.add((B,D))
 result_counts=Counter()
 for B,D in sorted(cases):
  vals={v:score(g[v],B,D) for v in pop}
  eta=min(vals.values())
  full={v for v,vv in vals.items() if 2*vv<3*eta}
  pred=predicted(B,D)
  assert full==pred,(B,D,eta,sorted(full),sorted(pred))
  assert eta==min(vals[v] for v in W)
  # Check analytic score simplifications in bridge strip.
  assert vals[b]==vals[e]==Q(12,B+D)
  assert vals[f]==Q(3,B+176)
  assert vals[a]==max(Q(1,104),Q(7,D+136),Q(2,B+176),Q(6,B+D))
  assert vals[d]==max(Q(2,B+136),Q(1,104),Q(6,B+D),Q(7,D+176))
  result_counts[len(full)]+=1
 print('R151 EXACT BRIDGE SIX-DIRECTION ATLAS PASS')
 print('population',len(pop),'full-exact-cases',len(cases),'counts_observed',dict(sorted(result_counts.items())))
 print('B=32 equality and B=32+ jump, all threshold equalities checked by Fraction')

if __name__=='__main__': main()
