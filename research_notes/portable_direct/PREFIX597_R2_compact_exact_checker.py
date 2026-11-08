#!/usr/bin/env python3
"""PREFIX597 R2 complete-port exact integer checker, no third-party dependencies."""
from itertools import product
from collections import defaultdict
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in STAR[a] for t in (-1,1) for p in near(a,t*k))
IX={p:i for i,p in enumerate(P)}
def next_phase(i):
 a,p,c=P[i]; b=next(b for b in range(4) if b!=a and abs(c) in STAR[b])
 return tuple(IX[z] for z in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(next_phase(i) for i in range(48));G=IX[(0,1,-3)]
ax=tuple(abs(z[2])-1 for z in P)
assert len(P)==48 and G==4 and all(len(z)==3 for z in N)
E=[[] for _ in range(7)]
for i in range(48):
 for j in N[i]:
  for u,v in product((0,1),repeat=2):E[6 if j==G and u==v==1 else ax[i]].append((2*i+u,2*j+v))
assert list(map(len,E))==[93,96,96,96,96,96,3]
def edge_step(r,x,z):
 out=[0]*96; w=(*x,x[0]*z)
 for k in range(7):
  for i,j in E[k]:out[i]+=w[k]*r[j]
 return out
def native_step(r,x,z):
 s=[r[2*j]+r[2*j+1] for j in range(48)];out=[0]*96
 for i in range(48):
  t=x[ax[i]]*sum(s[j] for j in N[i]);out[2*i]=t
  out[2*i+1]=t+(x[0]*(z-1)*r[2*G+1] if G in N[i] else 0)
 return out
def c48(r):return [r[2*j] if j==G else r[2*j]+r[2*j+1] for j in range(48)]
def q48(v,x,z):
 out=[]
 for i in range(48):
  out.append(x[ax[i]]*sum(v[j] if i==G else ((3+z)*v[j] if j==G else 2*v[j]) for j in N[i]))
 return out
def o48(v,x,z):
 out=[0]*96
 for i in range(48):
  s=sum(v[j] for j in N[i] if j!=G)
  out[2*i]=x[ax[i]]*(s+(2*v[G] if G in N[i] else 0))
  out[2*i+1]=x[ax[i]]*(s+((1+z)*v[G] if G in N[i] else 0))
 return out
def tail(r,seq):
 if not seq:return r[:]
 if len(seq)==1:return native_step(r,*seq[0])
 v=c48(native_step(r,*seq[0]))
 for x,z in seq[1:-1]:v=q48(v,x,z)
 return o48(v,*seq[-1])
# A_k = B_k C_49, M_k=C_49 B_k: positive exact source-bit realization.
key=[(j,None) for j in range(48) if j!=G]+[(G,0),(G,1)]
slot={entry:m for m,entry in enumerate(key)}
B=[defaultdict(int) for _ in range(7)]
for k in range(7):
 for i,j in E[k]:
  phase,bit=divmod(j,2)
  if phase!=G and bit==1:continue
  B[k][i,slot[(phase,bit if phase==G else None)]]+=1
M=[defaultdict(int) for _ in range(7)]
for k in range(7):
 for (i,m),v in B[k].items():
  phase,bit=divmod(i,2)
  M[k][slot[(phase,bit if phase==G else None)],m]+=v
assert sum(map(len,M))==153 and sum(map(len,B))==294
Q=[defaultdict(int) for _ in range(7)]
for i in range(48):
 for j in N[i]:
  Q[ax[i]][i,j]=1 if i==G else (3 if j==G else 2)
  if i!=G and j==G:Q[6][i,j]=1
assert sum(map(len,Q))==147 and len(set(p for c in Q for p in c))==144
def spmv(coeff,v,x,z,n):
 out=[0]*n;w=(*x,x[0]*z)
 for k in range(7):
  for (i,j),a in coeff[k].items():out[i]+=a*w[k]*v[j]
 return out
def pos49(r,seq):
 if not seq:return r[:]
 w=[r[2*j]+r[2*j+1] if bit is None else r[2*j+bit] for j,bit in key]
 for x,z in seq[:-1]:w=spmv(M,w,x,z,49)
 return spmv(B,w,*seq[-1],96)
def sparse_tail(r,seq):
 if len(seq)<2:return direct(r,seq)
 v=c48(native_step(r,*seq[0]))
 for x,z in seq[1:-1]:v=spmv(Q,v,x,z,48)
 return o48(v,*seq[-1])
def direct(r,seq):
 for x,z in seq:r=edge_step(r,x,z)
 return r
S=[[(1,1,1,1,1,1),1]]*12
S=[(tuple(x),z) for x,z in S]
SEQ=[S,[(tuple(1+((t+3*i)%4) for i in range(6)),t%6) for t in range(12)],
   [((1,0,2,0,3,1),0),((0,1,2,1,0,3),2),((1,3,0,0,2,4),5)]*4]
V=[[int(i==j) for i in range(96)] for j in range(96)]+[[1]*96,
  [(17*i+9)%19 for i in range(96)],[0]*96,[int(i%5==0) for i in range(96)]]
count=0
for r in V:
 for seq in SEQ:
  for d in (0,1,2,3,6,12):
   src=direct(r,seq[:d]); t=tail(r,seq[:d]);p=pos49(r,seq[:d]);q=sparse_tail(r,seq[:d])
   assert src==t==p==q
   assert all(v>=0 for v in t)
   count+=1
assert count==1800
print('ALL_ASSERTIONS_PASS',count,'source_edges',sum(map(len,E)),
 '49_coeff_nnz',sum(map(len,M)),'48_coeff_nnz',sum(map(len,Q)))
