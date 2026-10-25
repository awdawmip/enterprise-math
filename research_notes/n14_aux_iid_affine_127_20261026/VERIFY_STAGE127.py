"""Stage127 exact Fraction Bellman + four-corner observer verifier. Stdlib only."""
from fractions import Fraction as F
import json
N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(8246448,11561);L=F(7673768,11561)
B=(11,0,1);C=(11,6,2);R=(0,0,0)
def kids(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
H={};ACT={};TIES={};GAPS=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a)
   c={'P':K*r,'Q':L}
   if n<N:c['C']=1+sum(P[j]*H[z] for j,z in enumerate(kids(s)))
   v=min(c.values());H[s]=v
   opts=[k for k in ('P','Q','C') if k in c and c[k]==v]
   ACT[s]='C' if s in (B,C) else opts[0]
   assert ACT[s] in opts
   if len(opts)>1:TIES[s]=opts
   GAPS.extend(q-v for q in c.values() if q>v)
assert len(H)==680 and len(GAPS)==1238 and min(GAPS)==F(71,9459)
assert TIES=={B:['Q','C'],C:['P','C']}
assert H[R]==F(207290753323284460123369,422211736708250075136)
STOP={'P':(F(0),F(1),F(0),F(0)),'Q':(F(1),F(0),F(0),F(0))}
def corner(w,u):
 M={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    s=(n,a,b);cost=dict(STOP)
    if n<N:
     v=[M[z] for z in kids(s)]
     cost['C']=(sum(P[j]*v[j][0] for j in range(3)),
                sum(Q[j]*v[j][1] for j in range(3)),
                1+sum(P[j]*v[j][2] for j in range(3)),
                1+sum(Q[j]*v[j][3] for j in range(3)))
    action='Q' if s==B and w else 'P' if s==C and u else ACT[s]
    M[s]=cost[action]
 return M[R]
M00=corner(0,0);M10=corner(1,0);M01=corner(0,1);M11=corner(1,1)
dB=tuple(x-y for x,y in zip(M10,M00))
dC=tuple(x-y for x,y in zip(M01,M00))
assert M11==tuple(M00[i]+dB[i]+dC[i] for i in range(4))
assert M00==(F(1216989348409665853,3505953353861431296),F(24784784228981,71328803586048),F(5568467048798569363,438244169232678912),F(645856546493993,53496602689536))
assert dB==(F(4619140625,2229025112064),-F(751953125,417942208512),-F(25673828125,278628139008),-F(17939453125,104485552128))
assert dC==(-F(3026375,112717121716224),F(3026375,80244904034304),-F(42644375,4696546738176),-F(22835375,6687075336192))
diff=lambda x:x[0]-x[1]
w0=-diff(M00)/diff(dB)
slope=-diff(dC)/diff(dB)
assert w0==F(1232366013208259,13573120000000000)
assert slope==F(3858353,231360000000)
assert 0<w0<w0+slope<1
M=lambda u:tuple(M00[i]+(w0+slope*u)*dB[i]+u*dC[i] for i in range(4))
lo,hi=M(F(0)),M(F(1));eta=hi[0]-lo[0]
assert lo[0]==lo[1]==F(18340838011402083499,52808422392537808896)
assert lo[2]==F(335279238082246223695,26404211196268904448)
assert eta==F(3180720125,412565799941701632)>0
assert hi[0]==hi[1]==F(18340838418534259499,52808422392537808896)
assert hi[2]==F(335278957759082895695,26404211196268904448)
assert lo[2]-lo[3]==F(16916724390710645177,26404211196268904448)>0
assert hi[2]-hi[3]==F(50749829511513535531,79212633588806713344)>0
assert hi[2]==lo[2]-(K+L)*eta
assert H[R]==lo[2]+L*lo[0]+K*lo[1]
assert H[R]==hi[2]+L*hi[0]+K*hi[1]
print(json.dumps({'status':'PASS','states':len(H),'strict_positive_gaps':len(GAPS),'min_gap':str(min(GAPS)),
'ties':{str(s):a for s,a in TIES.items()},'root':str(H[R]),
'corners':{k:list(map(str,v)) for k,v in [('00',M00),('10',M10),('01',M01),('11',M11)]},
'dB':list(map(str,dB)),'dC':list(map(str,dC)),'w0':str(w0),'dw_du':str(slope),'eta127':str(eta),
'alpha127':str(hi[0]),'V127':str(hi[2])},indent=2))
