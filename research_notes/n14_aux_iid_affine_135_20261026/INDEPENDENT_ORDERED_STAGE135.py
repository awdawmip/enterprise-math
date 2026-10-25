"""Second author implementation: top-down exact integer-mass ordered-history DFS for Stage135.
No import or call into the primary checker.
"""
from functools import cache
from fractions import Fraction as F
from collections import defaultdict
import json
PN=(3,1,20);QN=(1,1,10)
p=tuple(F(x,24) for x in PN)
K=F(119895901488,209680375);L=F(113419128664,209680375)
B=(11,0,1);A=(7,3,0)
@cache
def optimum(n,a,b):
 vals={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14: vals['C']=1+sum(p[j]*optimum(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
 least=min(vals.values());return least,tuple(x for x in ('P','Q','C') if x in vals and vals[x]==least)
obs={};visits={};terminal={};first_hit={}
for w in (0,1):
 for u in (0,1):
  accum=[0,0,0,0,0,0]
  hits=defaultdict(lambda:[0,0,0])
  def dfs(n,a,b,wp,wq):
   accum[4]+=1
   s=(n,a,b)
   if s in (A,B):
    hits[s][0]+=1
    hits[s][1]+=wp*24**(14-n)
    hits[s][2]+=wq*12**(14-n)
   admissible=optimum(n,a,b)[1]
   action=('Q' if w else 'C') if s==B else ('P' if u else 'C') if s==A else admissible[0]
   assert action in admissible,(s,action,admissible)
   if action=='C':
    for j in range(3):dfs(n+1,a+(j==0),b+(j==1),wp*PN[j],wq*QN[j])
   else:
    accum[5]+=1
    pnum=wp*24**(14-n);qnum=wq*12**(14-n)
    if action=='Q': accum[0]+=pnum
    else:accum[1]+=qnum
    accum[2]+=n*pnum;accum[3]+=n*qnum
  dfs(0,0,0,1,1)
  tag=f'{w}{u}'
  obs[tag]=tuple(F(accum[j],(24 if j in (0,2) else 12)**14) for j in range(4))
  visits[tag]=accum[4];terminal[tag]=accum[5]
  if tag=='00':first_hit={str(s):{'words':v[0],'P':str(F(v[1],24**14)),'Q':str(F(v[2],12**14))} for s,v in hits.items()}
assert optimum.cache_info().currsize==680
add=lambda u,v:tuple(x+y for x,y in zip(u,v))
sub=lambda u,v:tuple(x-y for x,y in zip(u,v))
scale=lambda u,t:tuple(x*t for x in u)
M00=obs['00'];dB=sub(obs['10'],M00);dA=sub(obs['01'],M00)
assert obs['11']==add(add(M00,dB),dA)
assert dB==tuple(F(x) for x in ('4619140625/2229025112064','-751953125/417942208512','-25673828125/278628139008','-17939453125/104485552128'))
assert dA==tuple(F(x) for x in ('-128337803125/760840571584512','4604665625/20061226008576','-1268240553125/31701690482688','-7877209375/557256278016'))
D=lambda v:v[0]-v[1]
w0=-D(M00)/D(dB);slope=-D(dA)/D(dB)
assert w0==F(29128806260109437,81438720000000000)
assert slope==F(2617695451,25449600000)
lo=add(M00,scale(dB,w0));hi=add(add(M00,scale(dB,w0+slope)),dA)
assert 0<w0<w0+slope<1
assert lo[0]==lo[1] and hi[0]==hi[1]
assert lo[2]>lo[3] and hi[2]>hi[3]
assert lo[0]==F(36703016772992738695,105616844785075617792)
assert lo[2]==F(656399729826573779227,52808422392537808896)
assert hi[0]==F(12235904537797579565,35205614928358539264)
assert hi[2]==F(72642955720985708803,5867602488059756544)
assert hi[2]+(K+L)*hi[0]==optimum(0,0,0)[0]
if __name__=='__main__':
 print(json.dumps({'status':'PASS','states':680,'visits':visits,'terminal_histories':terminal,'first_hits':first_hit,
 'corners':{x:list(map(str,v)) for x,v in obs.items()},'M00':list(map(str,M00)),'dB':list(map(str,dB)),'dA':list(map(str,dA)),
 'w0':str(w0),'slope':str(slope),'alpha135':str(hi[0]),'V135':str(hi[2])},indent=2))
