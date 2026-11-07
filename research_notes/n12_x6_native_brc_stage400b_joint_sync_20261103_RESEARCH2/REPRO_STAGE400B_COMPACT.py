#!/usr/bin/env python3
# Stage400-B source-tagged synchronized BRC histogram DP; exact integers only.
from collections import defaultdict
from itertools import product
A=(1,-1,2,-2)
D=tuple(x for i in range(1,7) for x in (i,-i))
def z(w):return tuple(w.count(i)-w.count(-i) for i in range(1,7))
def J(w):
 d=defaultdict(int)
 for a,b in zip(w,w[1:]):d[(a,b)]+=1
 return tuple(sorted((a,b,n) for (a,b),n in d.items()))
def S(c,w):
 if c==0:return (w[-1],) if w else (0,)
 if not w:return (S(c-1,w),None,None)
 return (S(c-1,w),S(c-1,w[:-1]),S(c-1,w[:-2]) if len(w)>1 and w[-1]==-w[-2] else None)
def K(w,v):return sum(a==b for a,b in zip(w,v))
def groups(m):
 d=defaultdict(list)
 for w in product(A,repeat=m):d[(z(w),J(w))].append(w)
 return d
def dp(jp,jq,m,c,zp,zq):
 if m==0:return {(0,S(c,()),S(c,())):1}
 p={(a,b):n for a,b,n in jp};q={(a,b):n for a,b,n in jq}
 pk=tuple(sorted(p));qk=tuple(sorted(q));pi={e:i for i,e in enumerate(pk)};qi={e:i for i,e in enumerate(qk)}
 basep=tuple(p[e] for e in pk);baseq=tuple(q[e] for e in qk)
 letters=sorted({x for a,b in list(p)+list(q) for x in (a,b)}) if m>1 else list(A)
 k=min(m,2*c+1);state=defaultdict(int)
 for a in letters:
  for b in letters:state[(basep,baseq,a,b,(a,),(b,),int(a==b))]+=1
 for _ in range(1,m):
  nxt=defaultdict(int)
  for (rp,rq,a,b,u,v,r),n in state.items():
   for aa in letters:
    i=pi.get((a,aa))
    if i is None or rp[i]==0:continue
    rp2=list(rp);rp2[i]-=1
    for bb in letters:
     j=qi.get((b,bb))
     if j is None or rq[j]==0:continue
     rq2=list(rq);rq2[j]-=1
     nxt[(tuple(rp2),tuple(rq2),aa,bb,(u+(aa,))[-k:],(v+(bb,))[-k:],r+int(aa==bb))]+=n
  state=nxt
 def endpoint(hist,t):
  counts=defaultdict(int)
  for a,b,n in hist:counts[a]+=n
  counts[t]+=1
  return tuple(counts[i]-counts[-i] for i in range(1,7))
 out=defaultdict(int)
 for (rp,rq,a,b,u,v,r),n in state.items():
  if not any(rp) and not any(rq) and endpoint(jp,a)==zp and endpoint(jq,b)==zq:out[(r,S(c,u),S(c,v))]+=n
 return dict(out)
def brute(f,g,c):
 out=defaultdict(int)
 for w in f:
  for v in g:out[(K(w,v),S(c,w),S(c,v))]+=1
 return dict(out)
def brc(weights):
 cur={(0,0,0,0,0,0):1}
 for step in range(4):
  nxt=defaultdict(int)
  for point,n in cur.items():
   for d in D:
    pos=list(point);pos[abs(d)-1]+=1 if d>0 else -1
    nxt[tuple(pos)]+=n*weights.get(d,1)
  cur=nxt
 return cur[(2,0,0,0,0,0)]
def main():
 checks=0; sizes={};nontrivial4=[]
 for m in range(6):
  gg=groups(m);dups=[(key,items) for key,items in gg.items() if len(items)>1]
  sizes[m]=(len(gg),len(dups))
  if m<4:assert not dups
  if m==4:nontrivial4=dups
  for (endpoint,j),f in gg.items():
   if m<=3 or len(f)>1:
    for c in (0,1,2):
     assert dp(j,j,m,c,endpoint,endpoint)==brute(f,f,c)
     checks+=1
 for (kp,f),(kq,g) in product(nontrivial4,repeat=2):
  assert dp(kp[1],kq[1],4,1,kp[0],kq[0])==brute(f,g,1)
  checks+=1
 w=(1,1,-1,1);v=(1,-1,1,1)
 assert groups(4)[(z(w),J(w))]==[w,v]
 assert [[K(a,b) for b in (w,v)] for a in (w,v)]==[[4,2],[2,4]]
 assert S(1,w)!=S(1,v)
 assert (brc({}),brc({1:2,-1:3}))==(64,336)
 print('STAGE400B_COUPLED_TRANSFER_PASS',checks,'comparisons','fibers',sizes,'K',[[K(a,b) for b in (w,v)] for a in (w,v)],'BRC',(64,336))
if __name__=='__main__':main()
