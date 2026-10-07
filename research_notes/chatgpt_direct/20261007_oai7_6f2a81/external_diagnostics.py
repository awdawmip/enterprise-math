"""Bounded external mathematical diagnostics, NOT native-world/BRC execution.
The rational matrices are taken from the pinned OpenAI construction.tex formula.
No theorem-wide hitting-set assertion, original finite checker, or Lean proof is run.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

def matrix(i,d):
 return [[F((-1)**(r-q-1),r*i**(r-q)) if q<r else F(0) for q in range(d)] for r in range(d)]
def mul(A,B):
 return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def apply(A,x):return [sum((a*b for a,b in zip(row,x)),F(0)) for row in A]
def integral(i,x):
 d=len(x)
 return [F(0)]+[sum((x[q]*F((-1)**(r-q-1),i**(r-q)) for q in range(r)),F(0))/r for r in range(1,d)]
def ordered_word(word,d):
 x=[F(1)]+[F(0)]*(d-1)
 for i in reversed(word):x=apply(matrix(i,d),x)
 return x
checks=0
for d in range(1,9):
 for i in range(1,4):
  for q in range(d):
   x=[F(int(k==q)) for k in range(d)]
   assert apply(matrix(i,d),x)==integral(i,x);checks+=1
for length in range(5):
 for word in product(range(1,4),repeat=length):
  x=[F(1)]+[F(0)]*6
  for i in reversed(word):x=integral(i,x)
  assert ordered_word(word,7)==x; checks+=1
comm=[]
for d in [3,4]:
 A=mul(matrix(1,d),matrix(2,d));B=mul(matrix(2,d),matrix(1,d))
 C=[[a-b for a,b in zip(x,y)]for x,y in zip(A,B)]
 comm.append({'d':d,'nonzero_entries':[[r,q,str(C[r][q])] for r in range(d) for q in range(d) if C[r][q]]})
 assert (any(any(x) for x in C))==(d==4);checks+=1
assert comm[1]['nonzero_entries']==[[3,0,'-1/24']];checks+=1
roots={str(k):{'x2':[x for x in range(5**k) if x*x%(5**k)==0],'x2_minus5':[x for x in range(5**k) if (x*x-5)%(5**k)==0]}for k in [1,2,3]}
assert roots['1']['x2']==roots['1']['x2_minus5']==[0];checks+=1
assert len(roots['2']['x2'])==5 and roots['2']['x2_minus5']==[];checks+=1
assert len(roots['3']['x2'])==5 and roots['3']['x2_minus5']==[];checks+=1
out={'status':'PASS','scope':'bounded external formal-power-series and modular-arithmetic diagnostics, no native dynamics, no asymptotic theorem verification','exact_assertions':checks,'matrix_inputs':'i=1..3,d=1..8; words over 3 letters of length 0..4 at d=7','commutator':comm,'lifting_witness':roots,'source':'openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/construction.tex','original_triangular_checker_executed':False,'lean_executed':False,'actual_brc_executed':False,'independent_review':False}
p=Path(__file__).resolve().parent/'DIAGNOSTICS.json';p.write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
