from kf_final import jets
from fractions import Fraction as F
from math import prod
from collections import Counter

def values(d):
 J=list(range((d+1)//3+1,d//2+1))
 for j in J:
  T,_=jets(d,j);u=d-j;n=d-2*j
  D=2*u*(2*u+1)*(4*n+2)*prod(range(u+3,u+d+3))*prod(range(n+3,n+d+3))
  S=T*F(D**2,prod((k-j)**2 for k in J if k!=j))
  assert S.denominator==1
  yield j,S.numerator

def main():
 counts=Counter();maxbefore=0; survivors=[]
 for d in range(81,121):
  cand=list(range(max(64,(4*d*d+4)//5),4*d*d//3+1));counts['initial']+=len(cand)
  for i,(j,S) in enumerate(values(d)):
   if i==0:
    cand=[q for q in cand if S%(q+j)==0];counts['after_first']+=len(cand);maxbefore=max(maxbefore,len(cand))
   else: cand=[q for q in cand if S%(q+j)==0]
   if i==1:counts['after_second']+=len(cand)
   if not cand:counts['closed']+=1;counts['fibers_used']+=i+1;break
  if cand:survivors.append((d,cand))
 print(dict(counts));print('max_after_first',maxbefore);print('survivors',survivors)
if __name__=='__main__': main()
