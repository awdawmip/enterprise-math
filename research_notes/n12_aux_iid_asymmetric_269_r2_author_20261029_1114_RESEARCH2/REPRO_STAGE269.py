#!/usr/bin/env python3
"""Fully executable exact Stage269 Bellman/ordered-IID certificate (Python stdlib)."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
LP=F(132796528772096,960387801707);LQ=F(71829966906324,960387801707)
H=F(3311293384195030691817557,44598510985934255947776)
A=F(107398477982417,1408964021452800);B=F(28788331614361,37150418534400)
V=F(8204685878260270197067129,1427152351549896190328832)
S=[(i,j,n-i-j) for n in range(13) for i in range(n+1) for j in range(n-i+1)]
T=(0,0,5);U=(1,2,1)
assert len(S)==455

def step(s,k):return tuple(s[j]+int(j==k) for j in range(3))
def mass(s):
 i,j,k=s;return P[0]**i*P[1]**j*P[2]**k,Q[0]**i*Q[1]**j*Q[2]**k

def cert():
 bell,choices,ties,gaps={}, {},{},[]
 for s in S[::-1]:
  p,q=mass(s);cs={'P':LQ*q,'Q':LP*p}
  if sum(s)<12:cs['C']=q+sum(bell[step(s,k)] for k in range(3))
  z=min(cs.values());bell[s]=z;choices[s]=cs
  best=tuple(a for a,v in cs.items() if v==z)
  if len(best)>1:ties[s]=best
  gaps.extend(v-z for v in cs.values() if v>z)
 assert bell[0,0,0]==H and ties=={T:('P','C'),U:('Q','C')}
 assert sum(map(len,choices.values()))==1274 and len(gaps)==817
 assert min(gaps)==F(411190974797,3805739604133056507543552)
 return bell,choices

def policy(bell,choices,r,u):
 a={s:next(k for k,v in choices[s].items() if v==bell[s]) for s in S}
 a[T]='C' if r else 'P';a[U]='C' if u else 'Q'
 assert all(choices[s][v]==bell[s] for s,v in a.items())
 return a

def counts(a):
 arrivals=defaultdict(int);arrivals[0,0,0]=1
 o=[F(0)]*4;terminal=[F(0)]*2
 for s in S:
  m=arrivals[s]
  if not m:continue
  p,q=mass(s);z=a[s]
  if z=='P':o[1]+=m*q;terminal[0]+=m*p;terminal[1]+=m*q
  elif z=='Q':o[0]+=m*p;terminal[0]+=m*p;terminal[1]+=m*q
  else:
   assert sum(s)<12
   o[2]+=m*p;o[3]+=m*q
   for k in range(3):arrivals[step(s,k)]+=m
 assert terminal==[1,1] and arrivals[T]==1 and arrivals[U]==4
 return tuple(o)

def ordered(a):
 o=[F(0)]*4;terminal=[F(0)]*2;nodes=leaves=0
 def walk(word,p,q):
  nonlocal nodes,leaves
  nodes+=1;s=(word.count(0),word.count(1),word.count(2));z=a[s]
  if z=='P':o[1]+=q;terminal[0]+=p;terminal[1]+=q;leaves+=1
  elif z=='Q':o[0]+=p;terminal[0]+=p;terminal[1]+=q;leaves+=1
  else:
   assert len(word)<12
   o[2]+=p;o[3]+=q
   for k in range(3):walk(word+(k,),p*P[k],q*Q[k])
 walk((),F(1),F(1))
 assert terminal==[1,1]
 return tuple(o),nodes,leaves

def orient(x,y,z):return (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])

def main():
 bell,choices=cert();corners={};visits=ends=0
 for r,u in product((0,1),repeat=2):
  a=policy(bell,choices,r,u);o=counts(a);w,n,l=ordered(a)
  assert o==w and LP*o[0]+LQ*o[1]+o[3]==H and o[3]>o[2]
  corners[r,u]=o;visits+=n;ends+=l
 W,Z,C,D=corners[0,0],corners[1,0],corners[0,1],corners[1,1]
 assert all(D[i]-Z[i]==C[i]-W[i] for i in range(4))
 assert W[:2]==(F(378877764437,5283615080448),F(146176760405,185752092672))
 assert Z[:2]==(F(47509440493,587068342272),F(424845981215,557256278016))
 area=abs(orient(W,Z,C))
 assert area==F(15006059401671875,17251919966013638049792)
 L5=(F(378878551937,5283615080448),F(146176716655,185752092672))
 assert orient(W,Z,C)<0<orient(W,Z,L5)
 x=tuple(Z[i]-W[i] for i in range(4));y=tuple(C[i]-W[i] for i in range(4))
 det=x[0]*y[1]-x[1]*y[0];assert det!=0
 r=((A-W[0])*y[1]-(B-W[1])*y[0])/det
 u=(x[0]*(B-W[1])-x[1]*(A-W[0]))/det
 assert r==F(75294403653622137309,153662048273120000000)
 assert u==F(479208909,61464819309248000)
 assert 0<r<1 and 0<u<1
 w=tuple(W[i]+r*x[i]+u*y[i] for i in range(4))
 assert w[:2]==(A,B) and w[3]>w[2]
 assert w[3]==V==H-LP*A-LQ*B
 upper=F(53394354497531,9287604633600)
 assert upper-V==F(428502556554481,11892936262915801586073600)>0
 assert visits==7288 and ends==4860
 print('STAGE269_EXACT_ALL_REAL_FACE_PASS')
 print('states=455 actions=1274 positive_gaps=817 ties=',T,U)
 print('lambdaP=',LP,'lambdaQ=',LQ,'H=',H)
 print('area=',area,'r=',r,'u=',u)
 print('opt=',V,'gap_prior_feasible_upper=',upper-V)
 print('ordered_nodes=',visits,'terminal_leaves=',ends,'P_Q_terminal_mass=1_each')
 for label,o in zip(('W','Z','C','D'),(W,Z,C,D)):
  print(label,','.join(map(str,o)))
if __name__=='__main__':main()
