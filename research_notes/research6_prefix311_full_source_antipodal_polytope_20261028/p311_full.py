#!/usr/bin/env python3
"""Exact BRC port antipodal noise certificates. Source: PREFIX299 RESULTS json
Git blob b6acffe158f014469235f5428d2889ff43b62810.
No pi/trig/matrix exponential; BRC ports and each labelled path kept explicitly.
Variables: v in Q(i)^3, a_+=v/2 and a_-=-v/2.
B integer real/imag part of A5(1). All reference intervals intersect
iff -8 <= (Bv)_k <= 8 at epsilon=1. Global max over a convex polytope
occurs at a vertex, each vertex binds six independent real rows.
"""
from itertools import combinations,product
from sympy import Matrix, Rational
import json
S4=[[[[-5,2],[0,0],[2,0]],[[-4,1],[4,0],[-2,1]],[[-1,0],[0,-4],[-1,-6]]],[[[-5,-2],[0,0],[2,0]],[[-4,-1],[4,0],[-2,-1]],[[-1,0],[0,4],[-1,6]]],[[[-5,-2],[0,0],[2,0]],[[-3,2],[4,0],[1,4]],[[-2,1],[0,-4],[-4,-3]]],[[[-5,2],[0,0],[2,0]],[[-3,-2],[4,0],[1,-4]],[[-2,-1],[0,4],[-4,3]]],[[[-5,-2],[0,0],[2,0]],[[-3,1],[0,0],[-5,3]],[[-2,-2],[4,4],[2,2]]],[[[-5,2],[0,0],[2,0]],[[-3,-1],[0,0],[-5,-3]],[[-2,-2],[4,4],[2,2]]]]
S7=[[[[-6,1],[4,0],[0,1]],[[-2,0],[0,0],[5,-2]],[[-2,1],[-4,0],[-4,1]]],[[[-6,-1],[4,0],[0,-1]],[[-2,-1],[-4,0],[-4,-1]],[[-2,0],[0,0],[5,2]]],[[[-5,3],[0,0],[-3,1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,-2]]],[[[-5,-3],[0,0],[-3,-1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,-2]]],[[[-4,-3],[0,4],[-2,1]],[[-4,1],[0,-4],[-2,-3]],[[-2,0],[0,0],[5,2]]],[[[-4,-1],[0,4],[-2,3]],[[-4,3],[0,-4],[-2,-1]],[[-2,0],[0,0],[5,-2]]]]
E=[[(4,0),(4,0),(0,0)],[(0,0),(-4,0),(4,0)]]

def bmatrix(M, omit=None):
  A=E+[[(a,b) for a,b in row] for j,row in enumerate(M) if omit is None or j!=omit]
  B=[]
  for row in A:
    B.extend(([(r) for re,im in row for r in (re,-im)], [(r) for re,im in row for r in (im,re)]))
  return B,A

def solve_case(M,omit=None):
  B,A=bmatrix(M,omit); n=len(B); assert n in (8,10)
  vertices=set(); nonsingular=0; candidates=0; feasible=0; maximizers=0
  best=Rational(-1); best_v=None; best_basis=None
  for ix in combinations(range(n),6):
    C=Matrix([B[i] for i in ix]); d=C.det()
    if d==0:continue
    nonsingular+=1
    inv=C.inv();F=Matrix(B)*inv
    for signs in product((-1,1),repeat=6):
      candidates+=1
      if any(abs(sum(F[r,c]*signs[c] for c in range(6)))>1 for r in range(n)): continue
      feasible+=1
      vv=tuple(8*sum(inv[i,c]*signs[c] for c in range(6)) for i in range(6))
      vertices.add(vv)
      gain=sum(t*t for t in vv)/4
      if gain>best:
        best=gain;best_v=vv;best_basis=(ix,signs)
  maximizers=sum(sum(t*t for t in v)/4==best for v in vertices)
  assert best_v is not None
  return {'omit':None if omit is None else 'R'+str(omit+1),'constraints':n,'rank6_subsets':nonsingular,'all_subsets':len(list(combinations(range(n),6))),'candidate_signs':candidates,'feasible_signs_with_duplicates':feasible,'vertices':len(vertices),'maximizers':maximizers,'gain_numerator':str(best.p),'gain_denominator':str(best.q),'gain':str(best),'witness_v':[str(v) for v in best_v],'readouts_Bv':[str(sum(B[i][j]*best_v[j] for j in range(6))) for i in range(n)], 'tight_basis':{'rows':list(best_basis[0]),'signs':list(best_basis[1])}}

if __name__=='__main__':
  import sys,time
  mode=sys.argv[1] if len(sys.argv)>1 else 'ten'
  rows=[];start=time.time()
  for name,models in [('S4',S4),('S7',S7)]:
    for i,M in enumerate(models):
      if mode=='ten':runs=[None]
      elif mode=='eight':runs=[0,1,2]
      elif mode=='both':runs=[None,0,1,2]
      else:raise ValueError(mode)
      for omit in runs:
        result=solve_case(M,omit)
        rows.append({'family':name,'orbit':i+1,**result})
        print(name,i+1,omit,result['gain'],'vertices',result['vertices'],flush=True)
  payload={'schema':'PREFIX311_EXACT_ANTIPODAL_BRC_POLYTOPE_V1','input_blob':'b6acffe158f014469235f5428d2889ff43b62810','instrument_A':'E=(4,4,0),C=(0,-4,4),M=PREFIX299; U=A/8','error':'eps=1; general eps by homogeneity and Q(i) density','q':'q=1; for q in C4 use unitary D(q)=diag(1,q,q^2) change of variables, same exact gain','method':'Enumerate all rank-six real constraint subsets and all 64 sign vectors, reject outside |Bv|<=8, take exact max ||v||^2/4. Every vertex included.','model':'static full 3-source Q(i)^3 BRC tagged five ports; full ten or eight reference menu','status':'AUTHOR_SIDE_EXACT_COMPUTATION_UNREVIEWED_NOT_ADMITTED','results':rows}
  out=str(__import__("pathlib").Path(__file__).resolve().parent / f"PREFIX311_RESULTS_{mode}.json")
  with open(out,'w') as f:json.dump(payload,f,ensure_ascii=False,indent=2)
  print('saved',out,'elapsed',round(time.time()-start,2))
