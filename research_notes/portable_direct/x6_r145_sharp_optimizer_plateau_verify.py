"""R145: exact sharp D boundary of eta=1/104 for B>=136, D>=528.

Preserves original six-pair Port-10 observer and full 1935 direction set.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product

A=[a for a in product(range(-10,11),repeat=3)
   if a != (0,0,0)
   and max(sum(max(v,0) for v in a),sum(max(-v,0) for v in a)) <= 10
   and next(v for v in a if v != 0)>0]

def gaps(a):
 x,y,z=a
 h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
 return tuple(abs(h[j]-h[i]) for i in range(4) for j in range(i+1,4))
G={a:gaps(a) for a in A}

def F(a,B,D):
 cap=(136+B,312,136+D,B+176,B+D,176+D)
 return max(Q(g,s) for g,s in zip(G[a],cap))

def eta(B,D):
 return min(F(a,B,D) for a in A)

def edge(B):
 return max(Q(1008),Q(1248)-B)

def main():
 assert len(A)==len(G)==1935
 b=(4,-1,0)
 witness=(9,-5,1)
 assert G[b]==(1,0,11,1,12,11)
 assert G[witness][1]==3 and F(witness,Q(136),Q(528))==Q(1,104)
 fixed=Counter()
 for a,g in G.items():
  if a==b: continue
  js=[j for j in (1,2,5) if 104*g[j]>=((312,1248,1288)[(1,2,5).index(j)])]
  assert js,('fixed-observation failure',a,g)
  fixed[js[0]]+=1
 assert sum(fixed.values())==1934, fixed
 assert fixed=={1:1920, 2:14},fixed
 # For b: at D<=1008 pair j=2 gives 11/(136+D)>=1/104;
 # on 1008<D<=1248-B pair j=4 gives 12/(B+D)>=1/104.
 assert 11*104==136+1008 and 12*104==1248
 # Beyond max(1008,1248-B), all six b ratios strictly <1/104.
 samples=0
 for B in [Q(136),Q(137),Q(150),Q(200),Q(239),Q(240),Q(241),Q(300),Q(1000000)]:
  E=edge(B)
  for D in [Q(528), (Q(528)+E)/2, E-Q(1,100), E, E+Q(1,100), E+Q(1)]:
   v=eta(B,D)
   if D<=E: assert v==Q(1,104),(B,D,v,'plateau')
   else:
    assert F(b,B,D)<Q(1,104),(B,D,F(b,B,D))
    assert v<Q(1,104),(B,D,v,'beyond')
   samples+=1
 print('R145 SHARP OPTIMIZER PLATEAU EXACT CERTIFICATE PASS')
 print('population',len(A),'B-independent_lower_certificates_excluding_b',sum(fixed.values()),'pair_counts',dict(fixed))
 print('sharp_plateau_boundary','max(1008,1248-B) for B>=136, D>=528', 'witness',witness,'exit_direction',b)
 print('full_fraction_cross_checks',samples)

if __name__=='__main__':main()
