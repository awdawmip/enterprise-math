from fractions import Fraction as F
from itertools import combinations
M=[[F(a,20) for a in r] for r in [(10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)]]
S=('AU','AU','AV','BU','BU','BV')
D1=tuple(F(x,40) for x in (5,5,10,2,8,10))
D2=[tuple(F(x,40) for x in r) for r in [(10,10,20,0,0,0),(0,0,0,4,16,20)]]
E=(0,0,0,1,1,1)
def tv(a,b):return sum((abs(a.get(x,F(0))-b.get(x,F(0))) for x in set(a)|set(b)),F(0))/2
def observe(row,eps,mask=0,sep=False):
 out={}
 for j,p in enumerate(row):
  if not p:continue
  s=S[j]
  if sep and s=='AV':key=(2,'Q',None);out[key]=out.get(key,F(0))+p;continue
  d=('P' if s in ('AU','BU') else 'Q') if sep else ('P' if mask>>j&1 else 'Q')
  if s!='BU':key=(3,d,None);out[key]=out.get(key,F(0))+p
  else:
   for z in (0,1):
    key=(3,d,z);out[key]=out.get(key,F(0))+p*(1-eps if z==j-3 else eps)
 assert sum(out.values())==1
 return out
def main():
 raw={'AU':((9,11),(10,10)),'AV':((5,5),(20,20)),'BU':((3,27),(15,15)),'BV':((30,30),(15,15))}
 for b in (0,1):
  a=[n for x in raw.values() for n in x[b] for _ in (0,1)]
  assert len(a)==16 and all(v>0 for v in a) and sum(a)==240
 assert all(sum(row)==1 for row in M+[D1]+D2)
 for i,row in enumerate(M):
  sup={'AU':(0,1),'AV':(2,),'BU':(3,4),'BV':(5,)}[S[i]]
  assert all(D1[j]<=row[j] and D2[E[i]][j]<=row[j] for j in sup)
  assert sum(D1[j] for j in sup)==F(1,4)
  assert sum(D2[E[i]][j] for j in sup)==F(1,2)
 n=0
 for eps in (F(0),F(1,8),F(1,4),F(1,2)):
  for mask in range(64):
   for i,row in enumerate(M):
    a=observe(row,eps,mask)
    assert tv(a,observe(D1,eps,mask))<=F(3,4)
    assert tv(a,observe(D2[E[i]],eps,mask))<=F(1,2)
    n+=1
  group_support={}
  for i,row in enumerate(M):
   a=observe(row,eps,sep=True); support={t for t,v in a.items() if v}
   if S[i] in group_support:assert support==group_support[S[i]]
   group_support[S[i]]=support
   assert tv(a,observe(D1,eps,sep=True))==F(3,4)
   assert tv(a,observe(D2[E[i]],eps,sep=True))==F(1,2)
   n+=1
  assert len(group_support)==4
  assert all(group_support[a].isdisjoint(group_support[b]) for a,b in combinations(group_support,2))
 assert n==1560
 print('PASS_BRC_N4_R1_R2_EXACT_FULL_TERMINAL_20261031')
 print('P/Q: 16 positive leaves each; normalization 240/240.')
 print('R1=3/4, R2=1/2 exact six-row source TV; 1560 rational terminal comparisons.')
 print('One lawful S23 policy has four disjoint provenance supports at 4 sensor error values.')
 print('Universal stochastic lower/causal-policy upper bounds are analytic in PROOF.md.')
if __name__=='__main__':main()
