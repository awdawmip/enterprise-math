"""Finite Fraction audit for the exact H* BRC observer-ablation proof."""
from fractions import Fraction as Q
M=[[Q(n,20) for n in r] for r in [
 (10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
 (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)]]
SRC=('AU','AU','AV','BU','BU','BV')
PREP=('AU_Q','AU_P','AV','BU_Q','BU_P','BV')
def hstar(row,eps,T,Z):
 out={}
 for i,p in enumerate(row):
  if not p:continue
  s=SRC[i];time=2 if s=='AV' else 3
  d='P' if s in ('AU','BU') else 'Q'
  values=((None,Q(1)),)
  if s=='BU' and Z:
   j=i-3;values=((0,1-eps if j==0 else eps),(1,1-eps if j==1 else eps))
  for z,pz in values:
   key=(time if T else None,d,z)
   out[key]=out.get(key,Q(0))+p*pz
 assert sum(out.values(),Q(0))==1
 return {k:v for k,v in out.items() if v}
def tv(x,y):
 return sum((abs(x.get(k,Q(0))-y.get(k,Q(0))) for k in set(x)|set(y)),Q(0))/2
def rank(matrix):
 a=[list(r) for r in matrix];m=len(a);n=len(a[0]);rr=0
 for j in range(n):
  p=next((i for i in range(rr,m) if a[i][j]),None)
  if p is None:continue
  a[rr],a[p]=a[p],a[rr];v=a[rr][j];a[rr]=[t/v for t in a[rr]]
  for i in range(m):
   if i!=rr and a[i][j]:
    v=a[i][j];a[i]=[t-v*u for t,u in zip(a[i],a[rr])]
  rr+=1
 return rr
def mix(*items):
 o={}
 for p,dist in items:
  for k,v in dist.items():o[k]=o.get(k,Q(0))+p*v
 assert sum(o.values(),Q(0))==1
 return o
def check(eps,T,Z):
 r=[hstar(row,eps,T,Z) for row in M]
 idx={s:i for i,s in enumerate(PREP)}
 a,v,bu,bv=(r[idx[s]] for s in ('AU_Q','AV','BU_Q','BV'))
 br={k:Q(1,5) if k[2]==0 else Q(4,5) if k[2]==1 else Q(1) for k in bu}
 assert sum(br.values(),Q(0))==1
 assert all(Q(1,2)*br.get(k,Q(0))<=row.get(k,Q(0))
            for row in (r[idx['BU_Q']],r[idx['BU_P']]) for k in br)
 if T and Z:
  groups=(v,a,br,bv)
  enc=(0,0,0,1,1,1)
  dec=[mix((Q(1,2),a),(Q(1,2),v)),mix((Q(1,2),br),(Q(1,2),bv))]
 elif T and not Z:
  assert a==r[idx['BU_Q']]==r[idx['BU_P']]
  groups=(v,a,bv);enc=(0,0,0,0,0,1)
  dec=[mix((Q(1,2),a),(Q(1,2),v)),bv]
 elif Z:
  assert v==bv
  groups=(v,a,br);enc=(0,0,0,1,1,0)
  dec=[mix((Q(1,2),a),(Q(1,2),v)),br]
 else:
  assert v==bv and a==r[idx['BU_Q']]==r[idx['BU_P']]
  groups=(v,a);enc=(1,1,0,1,1,0);dec=[v,a]
 c=mix(*((Q(1,len(groups)),g) for g in groups))
 x1=[tv(row,c) for row in r];x2=[tv(row,dec[enc[i]]) for i,row in enumerate(r)]
 R1=Q(len(groups)-1,len(groups));R2=Q(0) if len(groups)==2 else Q(1,2)
 assert all(z==R1 for z in x1) and max(x2)==R2
 atoms=sorted(set().union(*(row.keys() for row in r)),key=str)
 rr=rank([[row.get(k,Q(0)) for k in atoms] for row in r])
 exp={(True,True):4 if eps==Q(1,2) else 5,(True,False):3,
      (False,True):3 if eps==Q(1,2) else 4,(False,False):2}[(T,Z)]
 assert rr==exp
 return len(atoms),rr,len(groups),R1,R2
def main():
 raw={'AU':((9,11),(10,10)),'AV':((5,5),(20,20)),
      'BU':((3,27),(15,15)),'BV':((30,30),(15,15))}
 for b in (0,1):
  weights=[n for pair in raw.values() for n in pair[b] for _ in (0,1)]
  assert len(weights)==16 and min(weights)>0 and sum(weights)==240
 assert all(sum(r,Q(0))==1 for r in M)
 for eps in (Q(0),Q(1,8),Q(1,4),Q(1,2)):
  for T,Z in ((True,True),(True,False),(False,True),(False,False)):
   print('eps=%s T=%d Z=%d atoms,rank,G,R1,R2=%s'%(eps,T,Z,check(eps,T,Z)))
 print('PASS_BRC_N4_HSTAR_OBSERVER_ABLATION_EXACT_20261031')
 print('16 positive leaves per law, sum 240; 96 exact input-observer checks.')
 print('All-real epsilon and random-encoder statements follow from PROOF.md.')
if __name__=='__main__':main()
