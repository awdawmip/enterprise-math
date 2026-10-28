#!/usr/bin/env python3
"""Stage264 exact certificate: auxiliary ternary IID, not native P000."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
N=12
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
a=F(595553513081,6449725440000);b=F(2918481415,3869835264)
L=F(1357504,15355);M=F(859212,15355);H0=F(14999620027,268651080)
V0=F(16927184206983443,3094860441600000)
S=[(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
def child(s,z):return tuple(x+(k==z) for k,x in enumerate(s))
D={}; A={}; gaps=[];nact=0
for s in reversed(S):
 r=F(2,3)**s[0]*2**s[1]
 c={'P':M*r,'Q':L}
 if sum(s)<N:c['C']=r+sum(P[z]*D[child(s,z)] for z in range(3))
 m=min(c.values());D[s]=m;A[s]=[z for z in ('P','Q','C') if z in c and c[z]==m]
 gaps.extend(v-m for v in c.values() if v>m);nact+=len(c)
assert (len(S),nact,len(gaps),min(gaps),D[0,0,0])==(455,1274,817,F(250,27639),H0)
ties=[s for s in S if len(A[s])>1]
assert ties==[(0,0,5),(0,1,8)]

def policy(bits):
 d={s:A[s][0] for s in S}
 for s,z in zip(ties,bits):d[s]=A[s][z]
 return d

def dag(pol):
 mass=defaultdict(lambda:(F(0),F(0)));mass[0,0,0]=(F(1),F(1))
 v=[F(0)]*6
 for s in S:
  p,q=mass[s];z=pol[s]
  if z=='P':v[1]+=q;v[4]+=p;v[5]+=q
  elif z=='Q':v[0]+=p;v[4]+=p;v[5]+=q
  else:
   v[2]+=p;v[3]+=q
   for k in range(3):
    pp,qq=mass[child(s,k)];mass[child(s,k)]=(pp+p*P[k],qq+q*Q[k])
 assert v[4:]==[1,1]
 return tuple(v[:4])

def dfs(pol):
 v=[F(0)]*6;nodes=terms=0
 def go(w,p,q):
  nonlocal nodes,terms
  nodes+=1;z=pol[tuple(w.count(k) for k in range(3))]
  if z=='P':v[1]+=q;v[4]+=p;v[5]+=q;terms+=1
  elif z=='Q':v[0]+=p;v[4]+=p;v[5]+=q;terms+=1
  else:
   v[2]+=p;v[3]+=q
   for k in range(3):go(w+(k,),p*P[k],q*Q[k])
 go((),F(1),F(1))
 assert v[4:]==[1,1]
 return tuple(v[:4]),nodes,terms

B={};nodes=terms=0
for bits in product((0,1),repeat=2):
 k=tuple(bits);v=dag(policy(k));v2,nn,tt=dfs(policy(k));assert v==v2
 assert v[3]>v[2] and v[3]+L*v[0]+M*v[1]==H0
 B[k]=v;nodes+=nn;terms+=tt
 print('MASK',k,tuple(map(str,v)),nn,tt)
assert (nodes,terms)==(2659,1774)
G5,H5,G6,H6=(B[k] for k in ((0,0),(0,1),(1,0),(1,1)))
assert G5[:2]==(F(668435839,7739670528),F(2229900905,2902376448))
assert G6[:2]==(F(1524881053,15479341056),F(4295642435,5804752896))
assert H5[:2]==(F(3750849409,46438023168),F(13498546055,17414258688))
assert H6[:2]==(F(1420974803,15479341056),F(4343298685,5804752896))
def orient(u,v,w):return (v[0]-u[0])*(w[1]-u[1])-(v[1]-u[1])*(w[0]-u[0])
R=(G5,H5,H6,G6)
assert all(orient(R[i],R[(i+1)%4],R[(i+2)%4])>0 for i in range(4))
area=abs(sum(R[i][0]*R[(i+1)%4][1]-R[(i+1)%4][0]*R[i][1] for i in range(4)))/2
assert area==F(206182861328125,2495937495082991616)
F5=(F(4312568159,46438023168),F(13246202305,17414258688))
F6=(F(182851367,1719926784),F(471373465,644972544))
assert all(orient(G5,G6,x)<0 for x in (H5,H6))
assert all(orient(G5,G6,x)>0 for x in (F5,F6))
w=(F(16990664034839,37487792968750),F(705855264768,18743896484375),F(30536669447,59980468750))
assert sum(w)==1 and min(w)>0
x=tuple(sum(w[j]*v[i] for j,v in enumerate((G5,H5,G6))) for i in range(4))
assert x==(a,b,F(19540937843174179,4126480588800000),V0)
assert x[3]-x[2]==F(591724083257,806215680000)>0
assert H0-L*a-M*b==V0
print('BELLMAN',len(S),nact,len(gaps),'TIES',ties,'H',H0,'LP',L,'LQ',M)
print('CAPS',a,b,'V',V0,'TP',x[2],'AREA',area,'MIX',w)
print('ORDERED_DFS',nodes,terms)
print('STAGE264_EXACT_ALL_REAL_FACE_PASS')
