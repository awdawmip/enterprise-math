"""Stage128 separately authored literal ordered-branch integer numerator DFS."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14; wp=(3,1,20);wq=(1,1,10)
K=F(7794,11);L=F(7256,11)
B=(11,0,1);D=(12,2,0)
@lru_cache(None)
def bel(n,a,b):
 co={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:
  co['C']=1+sum(F(wp[j],24)*bel(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
 value=min(co.values())
 return value,tuple(x for x in co if co[x]==value)
assert bel(0,0,0)[0]==F(5444247642339796165,11158995049906176)
result={}
for w in (0,1):
 for u in (0,1):
  moments=[0,0,0,0];hits=defaultdict(lambda:[0,0,0]);visit=[0]
  def dfs(n,a,b,ip,iq):
   visit[0]+=1
   s=(n,a,b)
   if s in (B,D):
    h=hits[s];h[0]+=1;h[1]+=ip*24**(N-n);h[2]+=iq*12**(N-n)
   if s==B:act='Q' if w else 'C'
   elif s==D:act='P' if u else 'C'
   else:act=bel(n,a,b)[1][0]
   assert act in bel(n,a,b)[1]
   if act=='C':
    for j in range(3):
     dfs(n+1,a+(j==0),b+(j==1),ip*wp[j],iq*wq[j])
   else:
    mp=ip*24**(N-n);mq=iq*12**(N-n)
    if act=='Q':moments[0]+=mp
    else:moments[1]+=mq
    moments[2]+=n*mp;moments[3]+=n*mq
  dfs(0,0,0,1,1)
  M=(F(moments[0],24**N),F(moments[1],12**N),
     F(moments[2],24**N),F(moments[3],12**N))
  result[f'{w}{u}']=(M,visit[0],
    {k:(v[0],F(v[1],24**N),F(v[2],12**N)) for k,v in hits.items()})
M00=result['00'][0];M10=result['10'][0]
M01=result['01'][0];M11=result['11'][0]
dB=tuple(M10[i]-M00[i] for i in range(4))
dD=tuple(M01[i]-M00[i] for i in range(4))
assert M11==tuple(M00[i]+dB[i]+dD[i] for i in range(4))
w0=(M00[1]-M00[0])/(dB[0]-dB[1])
du=-(dD[0]-dD[1])/(dB[0]-dB[1])
assert w0==F(3697777109752777,40719360000000000) and du==F(50,241)
def balanced(u):
 w=w0+du*u
 return tuple(M00[i]+dB[i]*w+dD[i]*u for i in range(4))
left,right=balanced(F(0)),balanced(F(1))
assert left[0]==left[1]==F(18340838418534259499,52808422392537808896)
assert right[0]==right[1]==F(18348272658534259499,52808422392537808896)
assert right[2]==F(330193261759082895695,26404211196268904448)
assert left[2]>left[3] and right[2]>right[3]
assert result['00'][2][B]==(11,F(107421875,1451188224),F(107421875,725594112))
assert result['00'][2][D]==(66,F(107421875,644972544),F(107421875,1451188224))
assert {k:v[1] for k,v in result.items()}=={
 '00':789841,'01':789445,'10':789709,'11':789313}
print('PASS independent integer numerator ordered DFS; corners:',
      {k:v[1] for k,v in result.items()})
