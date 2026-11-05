from fractions import Fraction as F
from itertools import product
R=(F(1,2),F(1),F(3,2))
K=(F(1,16),F(7,8),F(1,16))
W=(F(1,2),F(1,2))
S=((F(1,4),F(3,4)),(F(1,2),F(1),F(3,2)),(F(5,4),F(7,4)))
M={
 'A':((F(1,2),F(1,2)),(F(1,4),F(1,2),F(1,4)),(F(1,2),F(1,2))),
 'B':((F(1,2),F(1,2)),(F(3,8),F(1,4),F(3,8)),(F(1,2),F(1,2)))
}
assert sum(K)==1 and sum(x*y for x,y in zip(R,K))==1
for h in M:
 for j,r in enumerate(R):
  assert len(S[j])==len(M[h][j]) and all(z>0 for z in M[h][j])
  assert sum(M[h][j])==1 and sum(s*z for s,z in zip(S[j],M[h][j]))==r
  assert all(s*z/r>0 for s,z in zip(S[j],M[h][j]))
a,b=F(5),-F(155,32); k=F(1)
def C(r): return max(-r,-k)
def c(r): return a*r+b
G0=sum(K[j]*C(R[j]) for j in range(3))-C(F(1))
G={(h,j):sum(M[h][j][i]*C(s) for i,s in enumerate(S[j]))-C(R[j]) for j in range(3) for h in M}
V={(h,j):G[h,j]-c(R[j]) for h in M for j in range(3)}
Y={h:G0-c(F(1))+sum(K[j]*max(F(0),V[h,j]) for j in range(3)) for h in M}
L=G0-c(F(1))+sum(K[j]*max(F(0),sum(W[i]*V[h,j] for i,h in enumerate(('A','B')))) for j in range(3))
BASE=C(F(1))-c(F(1))
FULL=BASE+sum(W[i]*max(F(0),Y[h]) for i,h in enumerate(('A','B')))
LR=BASE+max(F(0),L)
assert (G0,G['A',1],G['B',1])==(F(1,32),F(1,8),F(3,16))
assert Y=={'A':F(11,512),'B':F(25,512)} and L==F(11,512)
assert (FULL,LR,FULL-LR)==(F(-287,256),F(-581,512),F(7,512))
ratios=sorted(set(s for ss in S for s in ss))
assert len(ratios)==7
n=(-F(1),-k,-a,-b)
def obs(first,second,terminal,source_sensitive=False):
 eP=eQ=TP=TQ=F(0)
 for hi,h in enumerate(('A','B')):
  wh=W[hi]
  act1=first[h] if source_sensitive else first
  if act1<2:
   eP+=wh*int(act1==0);eQ+=wh*int(act1==1)
   TP+=wh;TQ+=wh
   continue
  for j,r in enumerate(R):
   q=wh*K[j];p=r*q
   act2=second[h,j] if source_sensitive else second[j]
   if act2<2:
    eP+=p*int(act2==0);eQ+=q*int(act2==1)
    TP+=2*p;TQ+=2*q
   else:
    for s,z in zip(S[j],M[h][j]):
     qs=q*z;ps=qs*s
     action=terminal[s]
     eP+=ps*int(action==0);eQ+=qs*int(action==1)
     TP+=3*ps;TQ+=3*qs
 return (eP,eQ,TP,TQ)
def dot(o):return sum(x*y for x,y in zip(n,o))
maximum=None;maximizers=0;total=0
for first in range(3):
 for second in product(range(3),repeat=3):
  for bits in product(range(2),repeat=len(ratios)):
   terminal=dict(zip(ratios,bits))
   val=dot(obs(first,second,terminal))
   total+=1
   if maximum is None or val>maximum:maximum=val;maximizers=1
   elif val==maximum:maximizers+=1
assert total==10368 and maximum==LR
first={'A':2,'B':2}
second={(h,0):2 for h in M}
second.update({('A',1):0,('B',1):2,('A',2):1,('B',2):1})
terminal={s:int(s>=1) for s in ratios}
O=obs(first,second,terminal,True)
assert O==(F(141,256),F(43,128),F(79,32),F(5,2)),O
assert dot(O)==FULL
assert (FULL-LR)/sum(abs(x) for x in n)==F(7,6064)
print('G0=',G0,'G_A_mid=',G['A',1],'G_B_mid=',G['B',1])
print('Y_A=',Y['A'],'Y_B=',Y['B'],'Y_LR=',L)
print('FULL=',FULL,'LR=',LR,'support_gap=',FULL-LR)
print('W=',tuple(str(x) for x in O))
print('seedless_deterministic_enumerated=',total,'maximizers=',maximizers)
print('distance_infty_lower=',F(7,6064))
print('PASS_EXACT_R5_TIMING_TILT_FULL_RIGIDITY')
