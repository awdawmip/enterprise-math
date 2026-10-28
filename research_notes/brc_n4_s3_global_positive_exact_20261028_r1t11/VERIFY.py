from fractions import Fraction as F
Q=F(0); O=F(1)
V={'P':(O,Q,Q),'Q':(Q,O,Q),'C':(Q,Q,O)}
N={1:{'A':(F(1,2),F(1,2)),'B':(F(1,2),F(3,2))},
   2:{'AU':(F(1,6),O),'AV':(F(1,3),F(1,4)),
      'BU':(F(1,4),O),'BV':(F(1,4),F(2))}}
for t in (3,4):
 N[t]={}
 for h,(q,r) in N[t-1].items():
  e=({'AU':F(1,10),'AV':Q,'BU':F(4,5),'BV':Q}[h] if t==3 else
     Q if h=='AV0' else F(3,50) if h=='AV1' else F(1,20))
  for j,s in enumerate((-1,1)):N[t][h+str(j)]=(q/2,r*(1+s*e))
for t in N:
 assert len(N[t])==2**t
 assert all(q>0 and r>0 for q,r in N[t].values())
 assert sum((q for q,r in N[t].values()),Q)==sum((q*r for q,r in N[t].values()),Q)==O
BASE={'AU0':'P','AU1':'P','AV0':'P','AV1':'C','BU0':'C','BU1':'P','BV0':'Q','BV1':'Q'}
F0={}; S={}
for t in (1,2):
 for h in N[t]: F0[t,h]=S[t,h]=V['C']
for h in N[3]:
 F0[3,h]=V[BASE[h]]
 S[3,h]=(F(1,2),Q,F(1,2)) if h in ('AV0','AV1') else F0[3,h]
for h,(q,r) in N[4].items():
 F0[4,h]=V['Q'] if r<F(2501,10000) else V['P']
 S[4,h]=(F(253,500),F(247,500),Q) if h in ('AV00','AV01') else F0[4,h]
for t in (3,4):
 d={}
 for h,(q,r) in N[t].items():
  if r in d:assert S[t,h]==d[r]
  d[r]=S[t,h]
def law(p):
 out=[Q]*16
 for h,(q,r) in N[4].items():
  z=O
  for t,k in enumerate((h[:1],h[:2],h[:3],h),1):
   v=p[t,k];assert sum(v,Q)==O and min(v)>=0
   if t==4:assert v[2]==0
   for j in (0,1):
    out[2*(t-1)+j]+=q*z*v[j]
    out[8+2*(t-1)+j]+=q*r*z*v[j]
   z*=v[2]
 return out
Y=law(F0); X=law(S)
assert Y==list(map(F,['0','0','0','0','11/24','1/4','1/12','5/24','0','0','0','0','13/30','1/2','53/2400','107/2400']))
tv=lambda a,b:sum((abs(x-y) for x,y in zip(a,b)),Q)/2
assert tv(Y[:8],X[:8])==tv(Y[8:],X[8:])==F(1,2000)
WQ=[F(1,10)]*4+[F(169,1750)]*2+[F(1,10),-F(1,10)]
WP=[F(2,5)]*4+[-F(697,1750)]*2+[-F(2,5),F(2,5)]
assert max(WQ)-min(WQ)+max(WP)-min(WP)==O
def c(t,h,a):
 r=N[t][h][1];j=2*(t-1)+(a=='Q')
 return WQ[j]+r*WP[j]
def v4(h):return sum(min(c(4,h+str(j),'P'),c(4,h+str(j),'Q'))/2 for j in (0,1))
def v3(h):
 hs=(h+'0',h+'1')
 if h in ('AV','BV'):
  return min(sum((v4(k) if a=='C' else c(3,k,a)) for k in hs)/2 for a in ('P','Q','C'))
 return sum(min(c(3,k,'P'),c(3,k,'Q'),v4(k)) for k in hs)/2
def v2(h):return min(c(2,h,'P'),c(2,h,'Q'),v3(h))
def v1(h):
 ch={'A':('AU','AV'),'B':('BU','BV')}[h]
 z=sum((N[2][k][0]/N[1][h][0])*v2(k) for k in ch)
 return min(c(1,h,'P'),c(1,h,'Q'),z)
assert [v2(h) for h in ('AU','AV','BU','BV')]==[-F(264,875),-F(3,1000),-F(5603,17500),-F(7,10)]
assert v1('A')==-F(359,3500) and v1('B')==-F(17853,35000)
minimum=(v1('A')+v1('B'))/2
full=sum(w*x for w,x in zip(WQ+WP,Y))
assert minimum==-F(21443,70000) and full==-F(10739,35000)
assert minimum-full==F(1,2000)
assert sum(w*x for w,x in zip(WQ+WP,X))==minimum
print('PASS_EXACT_N4_S3_D2_0_D3_D23_1_OVER_2000')
