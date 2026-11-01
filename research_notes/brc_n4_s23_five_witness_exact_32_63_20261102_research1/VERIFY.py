#!/usr/bin/env python3
"""Exact standalone five-policy two-free-decoder BRC/S23 theorem checker.

All arithmetic Fraction; no SciPy/LP trust needed for the certificate.
"""
from fractions import Fraction as F
from itertools import combinations
import json

M20=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1);B=(2,2,3,2,2,4);C=(5,6,7,8,9,10); GROUP=(0,0,1,2,2,3)
BASE=('34 24 34 24','34 23 34 34','34 34 34 23',
      '24 24 12 12','12 12 24 34','12 13 23 24',
      '23 34 12 13','24 34 12 14')

def prepared(z):
  latent=[]
  for x in range(6):
    a,b,c=z[A[x]],z[B[x]],z[C[x]]
    latent.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
  return tuple(tuple(sum((F(M20[i][x],20)*latent[x][t] for x in range(6)),F(0)) for t in range(4)) for i in range(6))

def decoder_rows(spec):
  ret=[]
  for pair in spec.split():
    v=[F(0)]*4
    for d in pair:v[int(d)-1]+=F(1,2)
    ret.append(tuple(v))
  return tuple(ret)

def decoded(D):
  return tuple(tuple(sum((F(M20[i][x],20)*D[GROUP[x]][t] for x in range(6)),F(0)) for t in range(4)) for i in range(6))

def tv(p,q):return sum((abs(p[t]-q[t]) for t in range(4)),F(0))/2

def loss(p,q):return max(tv(x,y) for x,y in zip(p,q))

def old(s,t):return (s,t,F(0),F(0),F(0),F(0),F(1),F(1),F(1),F(0),F(1))
def new(s,t):return (s,t,F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0))
POLICY={
 'W':(F(1),F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0),F(0)),
 'J':(F(1),F(1,3),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(1),F(0)),
 'A':old(F(1,7),F(1)),
 'B':old(F(1),F(1,7)),
 'C':new(F(1,7),F(1)),
}
P={k:prepared(v) for k,v in POLICY.items()}
# For every one of the ten triples, one original PURE prepared observation row
# has three pairwise disjoint events. In any one stochastic decoder, their three
# target probabilities must each be <= decoded center mass + r.
# The sum of target masses - 1 hence lower-bounds 3r.
CERT={
 ('W','J','A'):(6,('2','4','1')),
 ('W','J','B'):(6,('2','14','3')),
 ('W','J','C'):(6,('2','4','1')),
 ('W','A','B'):(6,('2','1','3')),
 ('W','A','C'):(3,('1','3','4')),
 ('W','B','C'):(6,('2','3','1')),
 ('J','A','B'):(6,('4','1','3')),
 ('J','A','C'):(3,('1','3','4')),
 ('J','B','C'):(6,('4','3','1')),
 ('A','B','C'):(3,('3','1','24')),
}
D9=((F(9,14),0,F(5,14),0),
    (F(9,14),0,0,F(5,14)),
    (F(1,2),0,0,F(1,2)),
    (F(1,2),F(1,2),0,0))
D10=((F(41,63),0,F(22,63),0),
     (F(41,63),0,F(22,63),0),
     (F(29,45),0,F(29,315),F(83,315)),
     (F(31,63),0,F(22,63),F(10,63)))

def main():
  assert set(CERT)==set(combinations(P,3))
  R=F(32,63)
  for k,p in P.items():
    assert all(all(x>=0 for x in row) and sum(row)==1 for row in p)
  dual=[]
  for trip,(i,events) in CERT.items():
    atoms=[]; target_sum=F(0)
    for k,s in zip(trip,events):
      subset={int(d)-1 for d in s}
      assert not any(subset & prior for prior in atoms)
      atoms.append(subset)
      target_sum+=sum((P[k][i-1][j] for j in subset),F(0))
    b=(target_sum-1)/3
    assert b>=R,(trip,b)
    dual.append({'witnesses':','.join(trip),'row':i,'events':list(events),'sum':str(target_sum),'certified_lower':str(b)})
  assert min(F(v['certified_lower']) for v in dual)==R
  FIXED=tuple(decoded(decoder_rows(v)) for v in BASE)
  NEW=(decoded(D9),decoded(D10))
  assert all(sum(row)==1 and min(row)>=0 for d in (D9,D10) for row in d)
  risk={}
  for name,p in P.items():
    all_risks=[loss(p,q) for q in FIXED+NEW]
    assert min(all_risks[:8])>R,(name,all_risks)
    risk[name]={'old_eight_min':str(min(all_risks[:8])),
                'new_9':str(all_risks[8]),'new_10':str(all_risks[9]),
                'bank_min':str(min(all_risks)),
                'six_row_errors_best_new':[str(tv(a,b)) for a,b in zip(p,NEW[0 if name in ('W','C') else 1])]}
    assert min(all_risks)<=R
  assert max(F(r['bank_min']) for r in risk.values())==R
  assert max(F(risk[k]['new_9']) for k in ('W','C'))<=R
  assert max(F(risk[k]['new_10']) for k in ('J','A','B'))<=R
  print(json.dumps({'model':'BRC_N4_S23_6_positive_sources_11_legal_controls',
    'input_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
    'fixed_decoders':[1,2,3,4,5,6,7,8], 'free_decoders':[9,10],
    'theorem':'EXACT_REAL_STOCHASTIC_TWO_DECODER_FIVE_POLICY_MINIMAX',
    'exact_radius':str(R),'triple_event_certificates':dual,'witness_risks':risk,
    'D9':[[str(x) for x in row] for row in D9],
    'D10':[[str(x) for x in row] for row in D10],
    'verification':'pure Python Fraction original six-source four-stop law; 10 triple disjoint-event lower certificates; 5 whole-source loss rows',
    'result':'PASS_BRC_N4_S23_FIVE_POINT_TWO_FREE_EXACT_32_63_20261102'
  },ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
