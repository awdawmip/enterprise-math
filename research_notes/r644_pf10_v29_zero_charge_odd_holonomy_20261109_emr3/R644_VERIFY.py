#!/usr/bin/env python3
"""R644 compact exact PF10 V29 conservative 3-PASS packet / V27 BRC score checker."""
from itertools import combinations
TRI=tuple(combinations(range(6),3))
NEI={s:tuple(t for t in TRI if len(set(s)&set(t))==2) for s in TRI}
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
def code(m,s):
 z=set(s);b=[]
 for i,j in m:
  if (i in z)+(j in z)!=1:return 0
  b.append(j in z)
 return 1 if sum(b)%2==0 else -1
C={s:tuple(code(m,s) for m in MATCH) for s in TRI}
assert len(C)==20 and len(set(C.values()))==20 and sum(map(len,NEI.values()))==180
class Cell:
 def __init__(self):
  self.m=[[0]*4 for _ in range(4)];self.ri=[0]*4;self.ro=[0]*4
 def PASS(self,i,j):self.m[i][j]+=1
 def obs(self):
  I=tuple(sum(self.m[i])+self.ri[i] for i in range(4))
  O=tuple(sum(self.m[j][i] for j in range(4))+self.ro[i] for i in range(4))
  u=tuple(I[i]-O[i] for i in range(4))
  om=tuple(tuple(self.m[i][j]-self.m[j][i] for j in range(4)) for i in range(4))
  return I,O,u,om
 def winners(self,s):
  u,om=self.obs()[2:]
  val={t:sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*om[i][j]*C[t][j] for i in range(4) for j in range(4)) for t in NEI[s]}
  m=max(val.values());return tuple(t for t in NEI[s] if val[t]==m),val
def TRANS(x,i,y,j):
 x.ro[i]+=1;y.ri[j]+=1
def Q(cells):return sum(sum(v.obs()[2]) for v in cells)
x,y=Cell(),Cell()
for i,j in ((0,1),(1,2),(2,0)):x.PASS(i,j);assert Q((x,y))==0
TRANS(x,0,y,0);assert Q((x,y))==0
TRANS(y,0,x,3);assert Q((x,y))==0
I,O,u,om=x.obs()
assert (I,O,u)==((1,1,1,1),(2,1,1,0),(-1,0,0,1))
assert om==((0,1,-1,0),(-1,0,1,0),(1,-1,0,0),(0,0,0,0))
LOOP=((0,1,2),(1,2,3),(2,3,4),(0,3,4),(0,3,5),(0,2,5))
def slope(s,t):return sum(C[s][i]*om[i][j]*C[t][j] for i in range(4) for j in range(4))
for i,s in enumerate(LOOP):
 w=LOOP[(i+1)%6];wins,val=x.winners(s)
 assert wins==(w,)
 assert min(val[w]-val[t] for t in NEI[s] if t!=w)==1
 assert slope(s,w)==max(slope(s,t) for t in NEI[s])==1
z=Cell()
for i,j in ((0,1),(1,2),(2,0)):z.PASS(i,j)
assert set(z.winners((0,1,2))[0])=={(0,1,5),(0,2,4),(1,2,3)}
S=LOOP[0];slots={k:i for i,k in enumerate(S)}
for n in range(151):
 I,O,u,og=x.obs()
 assert I==(n+1,n+1,n+1,1) and O==(n+2,n+1,n+1,0)
 assert u==(-1,0,0,1) and Q((x,y))==0
 assert all(og[i][j]==(n+1)*om[i][j] for i in range(4) for j in range(4))
 wins,val=x.winners(S);assert wins==(LOOP[(n+1)%6],)
 T=wins[0];com=set(S)&set(T)
 leave=next(iter(set(S)-com));enter=next(iter(set(T)-com))
 slots={**{i:slots[i] for i in com},enter:slots[leave]}
 if n==5:assert T==LOOP[0] and tuple(slots[i] for i in LOOP[0])==(2,1,0)
 if n==11:assert T==LOOP[0] and tuple(slots[i] for i in LOOP[0])==(0,1,2)
 S=T
 for i,j in ((0,1),(1,2),(2,0)):x.PASS(i,j)
 assert Q((x,y))==0
print('R644_V29_CONSERVATIVE_ZERO_Q_ODD_HOLONOMY_PASS', 'initial_gap',1,'primitive_seed_events',5,'verified_packets',151)
